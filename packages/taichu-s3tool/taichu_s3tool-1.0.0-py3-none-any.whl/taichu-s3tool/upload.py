# -*- coding: utf-8 -*-
# PROJECT LONGBOW - AMAZON S3 UPLOAD TOOL WITH BREAK-POINT RESUMING
import os
import sys
import json
import base64
from boto3.session import Session
from botocore.client import Config
from concurrent import futures
import time
import datetime
import hashlib
import logging
from pathlib import PurePosixPath, Path

global JobType, SrcFileIndex, DesProfileName, DesBucket, S3Prefix, MaxRetry, MaxThread, \
    MaxParallelFile, StorageClass, ifVerifyMD5, DontAskMeToClean, LoggingLevel, \
    SrcDir, SrcBucket, SrcProfileName, des_endpoint_url, src_endpoint_url, s3_dest_client, logger
max_get = 1000


def set_config(desBucket, s3Prefix, srcFileIndex, srcDir):
    global JobType, SrcFileIndex, DesProfileName, DesBucket, S3Prefix, MaxRetry, MaxThread, \
        MaxParallelFile, StorageClass, ifVerifyMD5, DontAskMeToClean, LoggingLevel, \
        SrcDir, SrcBucket, SrcProfileName, des_endpoint_url, src_endpoint_url
    JobType = 'LOCAL_TO_S3'
    des_endpoint_url = 'http://172.16.10.19:39999/api/v1/s3'
    DesBucket = desBucket
    S3Prefix = s3Prefix
    SrcFileIndex = srcFileIndex
    SrcDir = srcDir
    Megabytes = 1024 * 1024
    ChunkSize = 600 * Megabytes
    MaxRetry = 5
    MaxThread = 5
    MaxParallelFile = 5
    StorageClass = 'STANDARD'
    ifVerifyMD5 = False
    DontAskMeToClean = True
    LoggingLevel = 'INFO'

    S3Prefix = str(PurePosixPath(S3Prefix))  # 去掉结尾的'/'，如果有的话
    if S3Prefix == '/' or S3Prefix == '.':
        S3Prefix = ''

    return ChunkSize


# Configure logging
def set_log():
    logger = logging.getLogger()
    # File logging
    if not os.path.exists("./log"):
        os.system("mkdir log")
    this_file_name = os.path.splitext(os.path.basename(__file__))[0]
    file_time = datetime.datetime.now().isoformat().replace(':', '-')[:19]
    log_file_name = './log/' + this_file_name + '-' + file_time + '.log'
    print('Logging to file:', os.path.abspath(log_file_name))
    print('Logging level:', LoggingLevel)
    fileHandler = logging.FileHandler(filename=log_file_name, encoding='utf-8')
    fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s - %(message)s'))
    logger.addHandler(fileHandler)
    # Screen stream logging
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s - %(message)s'))
    logger.addHandler(streamHandler)
    # Loggin Level
    logger.setLevel(logging.WARNING)
    if LoggingLevel == 'INFO':
        logger.setLevel(logging.INFO)
    elif LoggingLevel == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    return logger, log_file_name


# Get local file list
def get_local_file_list(str_key=False):
    __src_file_list = []
    try:
        if SrcFileIndex == "*":
            for parent, dirnames, filenames in os.walk(SrcDir):
                for filename in filenames:  # 遍历输出文件信息
                    file_absPath = os.path.join(parent, filename)
                    file_relativePath = file_absPath[len(SrcDir) + 1:]
                    file_size = os.path.getsize(file_absPath)
                    key = Path(file_relativePath)
                    if str_key:
                        key = str(PurePosixPath(key))
                    __src_file_list.append({
                        "Key": key,
                        "Size": file_size
                    })
        else:
            join_path = os.path.join(SrcDir, SrcFileIndex)
            file_size = os.path.getsize(join_path)
            __src_file_list = [{
                "Key": SrcFileIndex,
                "Size": file_size
            }]
    except Exception as err:
        logger.error('Can not get source files. ERR: ' + str(err))
        input('PRESS ENTER TO QUIT')
        sys.exit(0)
    if not __src_file_list:
        logger.error('Source file empty.')
        input('PRESS ENTER TO QUIT')
        sys.exit(0)
    return __src_file_list


# Get object list on S3
def get_s3_file_list(*, s3_client, bucket, S3Prefix, no_prefix=False):
    logger.info('Get s3 file list ' + bucket)

    # For delete prefix in des_prefix
    if S3Prefix == '':
        # 目的bucket没有设置 Prefix
        dp_len = 0
    else:
        # 目的bucket的 "prefix/"长度
        dp_len = len(S3Prefix) + 1

    paginator = s3_client.get_paginator('list_objects_v2')
    __des_file_list = []
    try:
        response_iterator = paginator.paginate(
            Bucket=bucket,
            Prefix=S3Prefix
        )
        for page in response_iterator:
            if "Contents" in page:
                for n in page["Contents"]:
                    key = n["Key"]
                    if no_prefix:
                        key = key[dp_len:]
                    __des_file_list.append({
                        "Key": key,
                        "Size": n["Size"]
                    })
        logger.info(f'Bucket list length：{str(len(__des_file_list))}')
    except Exception as err:
        logger.error(str(err))
        input('PRESS ENTER TO QUIT')
        sys.exit(0)
    return __des_file_list


# Get all exist object list on S3
def get_uploaded_list(s3_client):
    logger.info('Get unfinished multipart upload')
    NextKeyMarker = ''
    IsTruncated = True
    __multipart_uploaded_list = []
    while IsTruncated:
        list_multipart_uploads = s3_client.list_multipart_uploads(
            Bucket=DesBucket,
            Prefix=S3Prefix,
            MaxUploads=1000,
            KeyMarker=NextKeyMarker
        )
        if "IsTruncated" not in list_multipart_uploads.keys() or "NextKeyMarker" not in list_multipart_uploads.keys():
            IsTruncated = False
            NextKeyMarker = ''
        else:
            IsTruncated = list_multipart_uploads["IsTruncated"]
            NextKeyMarker = list_multipart_uploads["NextKeyMarker"]
        if NextKeyMarker != '':
            for i in list_multipart_uploads["Uploads"]:
                __multipart_uploaded_list.append({
                    "Key": i["Key"],
                    "Initiated": i["Initiated"],
                    "UploadId": i["UploadId"]
                })
                logger.info(f'Unfinished upload, Key: {i["Key"]}, Time: {i["Initiated"]}')
    return __multipart_uploaded_list


# Jump to handle next file
class NextFile(Exception):
    pass


def uploadThread_small(srcfile, prefix_and_key):
    print(f'\033[0;32;1m--->Uploading\033[0m {srcfile["Key"]} - small file')
    with open(os.path.join(SrcDir, srcfile["Key"]), 'rb') as data:
        for retryTime in range(MaxRetry + 1):
            try:
                pstart_time = time.time()
                chunkdata = data.read()
                chunkdata_md5 = hashlib.md5(chunkdata)
                s3_dest_client.put_object(
                    Body=chunkdata,
                    Bucket=DesBucket,
                    Key=prefix_and_key,
                    ContentMD5=base64.b64encode(chunkdata_md5.digest()).decode('utf-8'),
                    StorageClass=StorageClass
                )
                pload_time = time.time() - pstart_time
                pload_bytes = len(chunkdata)
                pload_speed = size_to_str(int(pload_bytes / pload_time)) + "/s"
                print(f'\033[0;34;1m    --->Complete\033[0m {srcfile["Key"]} - small file - {pload_speed}')
                break
            except Exception as e:
                logger.warning(f'Upload small file Fail: {srcfile["Key"]}, '
                               f'{str(e)}, Attempts: {retryTime}')
                if retryTime >= MaxRetry:
                    logger.error(f'Fail MaxRetry Download/Upload small file: {srcfile["Key"]}')
                    return "MaxRetry"
                else:
                    time.sleep(5 * retryTime)
    return


def upload_file(*, srcfile, desFilelist, UploadIdList, ChunkSize_default):  # UploadIdList就是multipart_uploaded_list
    logger.info(f'Start file: {srcfile["Key"]}')
    prefix_and_key = srcfile["Key"]
    if JobType == 'LOCAL_TO_S3':
        prefix_and_key = str(PurePosixPath(S3Prefix) / srcfile["Key"])
    if srcfile['Size'] >= ChunkSize_default:
        try:
            # 循环重试3次（如果MD5计算的ETag不一致）
            for md5_retry in range(3):
                # 检查文件是否已存在，存在不继续、不存在且没UploadID要新建、不存在但有UploadID得到返回的UploadID
                response_check_upload = check_file_exist(srcfile=srcfile,
                                                         desFilelist=desFilelist,
                                                         UploadIdList=UploadIdList)
                if response_check_upload == 'UPLOAD':
                    logger.info(f'New upload: {srcfile["Key"]}')
                    response_new_upload = s3_dest_client.create_multipart_upload(
                        Bucket=DesBucket,
                        Key=prefix_and_key,
                        StorageClass=StorageClass
                    )
                    # logger.info("UploadId: "+response_new_upload["UploadId"])
                    reponse_uploadId = response_new_upload["UploadId"]
                    partnumberList = []
                elif response_check_upload == 'NEXT':
                    logger.info(f'Duplicated. {srcfile["Key"]} same size, goto next file.')
                    raise NextFile()
                else:
                    reponse_uploadId = response_check_upload

                    # 获取已上传partnumberList
                    partnumberList = checkPartnumberList(srcfile, reponse_uploadId)

                # 获取索引列表，例如[0, 10, 20]
                response_indexList, ChunkSize_auto = split(srcfile, ChunkSize_default)

                # 执行分片upload
                upload_etag_full, etag = uploadPart(uploadId=reponse_uploadId,
                                                    indexList=response_indexList,
                                                    partnumberList=partnumberList,
                                                    srcfile=srcfile,
                                                    ChunkSize_auto=ChunkSize_auto)

                # 合并S3上的文件
                response_complete = completeUpload(reponse_uploadId=reponse_uploadId,
                                                   srcfileKey=srcfile["Key"],
                                                   len_indexList=len(response_indexList),
                                                   upload_etag_full=etag)
                logger.info(f'FINISH: {srcfile["Key"]} TO {response_complete["Location"]}')

                # 检查文件MD5
                if ifVerifyMD5:
                    if response_complete["ETag"] == upload_etag_full:
                        logger.info(f'MD5 ETag Matched - {srcfile["Key"]} - {response_complete["ETag"]}')
                        break
                    else:  # ETag 不匹配，删除S3的文件，重试
                        logger.warning(f'MD5 ETag NOT MATCHED {srcfile["Key"]}( Destination / Origin ): '
                                       f'{response_complete["ETag"]} - {upload_etag_full}')
                        s3_dest_client.delete_object(
                            Bucket=DesBucket,
                            Key=prefix_and_key
                        )
                        UploadIdList = []
                        logger.warning('Deleted and retry upload {srcfile["Key"]}')
                    if md5_retry == 2:
                        logger.warning('MD5 ETag NOT MATCHED Exceed Max Retries - {srcfile["Key"]}')
                else:
                    break
        except NextFile:
            pass

    # Small file procedure
    else:
        # Check file exist
        for f in desFilelist:
            if f["Key"] == prefix_and_key and \
                    (srcfile["Size"] == f["Size"]):
                logger.info(f'Duplicated. {prefix_and_key} same size, goto next file.')
                return
        # 找不到文件，或文件Size不一致 Submit upload
        if JobType == 'LOCAL_TO_S3':
            uploadThread_small(srcfile, prefix_and_key)
    return


# Compare file exist on desination bucket
def check_file_exist(*, srcfile, desFilelist, UploadIdList):
    # 检查源文件是否在目标文件夹中
    prefix_and_key = srcfile["Key"]
    if JobType == 'LOCAL_TO_S3':
        prefix_and_key = str(PurePosixPath(S3Prefix) / srcfile["Key"])
    for f in desFilelist:
        if f["Key"] == prefix_and_key and \
                (srcfile["Size"] == f["Size"]):
            return 'NEXT'  # 文件完全相同
    # 找不到文件，或文件不一致，要重新传的
    # 查Key是否有未完成的UploadID
    keyIDList = []
    for u in UploadIdList:
        if u["Key"] == prefix_and_key:
            keyIDList.append(u)
    # 如果找不到上传过的Upload，则从头开始传
    if not keyIDList:
        return 'UPLOAD'
    # 对同一个Key（文件）的不同Upload找出时间最晚的值
    UploadID_latest = keyIDList[0]
    for u in keyIDList:
        if u["Initiated"] > UploadID_latest["Initiated"]:
            UploadID_latest = u
    return UploadID_latest["UploadId"]


# Check parts number exist on S3
def checkPartnumberList(srcfile, uploadId):
    try:
        prefix_and_key = srcfile["Key"]
        if JobType == 'LOCAL_TO_S3':
            prefix_and_key = str(PurePosixPath(S3Prefix) / srcfile["Key"])
        partnumberList = []
        PartNumberMarker = 0
        IsTruncated = True
        while IsTruncated:
            response_uploadedList = s3_dest_client.list_parts(
                Bucket=DesBucket,
                Key=prefix_and_key,
                UploadId=uploadId,
                MaxParts=1000,
                PartNumberMarker=PartNumberMarker
            )
            NextPartNumberMarker = response_uploadedList['NextPartNumberMarker']
            IsTruncated = response_uploadedList['IsTruncated']
            if NextPartNumberMarker > 0:
                for partnumberObject in response_uploadedList["Parts"]:
                    partnumberList.append(partnumberObject["PartNumber"])
            PartNumberMarker = NextPartNumberMarker
        if partnumberList:  # 如果为0则表示没有查到已上传的Part
            logger.info("Found uploaded partnumber: " + json.dumps(partnumberList))
    except Exception as checkPartnumberList_err:
        logger.error("checkPartnumberList_err" + json.dumps(checkPartnumberList_err))
        input('PRESS ENTER TO QUIT')
        sys.exit(0)
    return partnumberList


# split the file into a virtual part list of index, each index is the start point of the file
def split(srcfile, ChunkSize):
    partnumber = 1
    indexList = [0]
    if int(srcfile["Size"] / ChunkSize) + 1 > 10000:
        ChunkSize = int(srcfile["Size"] / 10000) + 1024  # 对于大于10000分片的大文件，自动调整Chunksize
        logger.info(f'Size excess 10000 parts limit. Auto change ChunkSize to {ChunkSize}')

    while ChunkSize * partnumber < srcfile["Size"]:  # 如果刚好是"="，则无需再分下一part，所以这里不能用"<="
        indexList.append(ChunkSize * partnumber)
        partnumber += 1
    return indexList, ChunkSize


# upload parts in the list
def uploadPart(*, uploadId, indexList, partnumberList, srcfile, ChunkSize_auto):
    partnumber = 1  # 当前循环要上传的Partnumber
    total = len(indexList)
    md5list = [hashlib.md5(b'')] * total
    complete_list = []
    # 线程池Start
    with futures.ThreadPoolExecutor(max_workers=MaxThread) as pool:
        for partStartIndex in indexList:
            # start to upload part
            if partnumber not in partnumberList:
                dryrun = False
            else:
                dryrun = True
            # upload 1 part/thread, or dryrun to only caculate md5
            if JobType == 'LOCAL_TO_S3':
                pool.submit(uploadThread,
                            uploadId=uploadId,
                            partnumber=partnumber,
                            partStartIndex=partStartIndex,
                            srcfileKey=srcfile["Key"],
                            total=total,
                            md5list=md5list,
                            dryrun=dryrun,
                            complete_list=complete_list,
                            ChunkSize=ChunkSize_auto)
            partnumber += 1
    # 线程池End
    logger.info(f'All parts uploaded - {srcfile["Key"]} - size: {srcfile["Size"]}')

    # Local upload 的时候考虑传输过程中文件会变更的情况，重新扫描本地文件的MD5，而不是用之前读取的body去生成的md5list
    if ifVerifyMD5 and JobType == 'LOCAL_TO_S3':
        md5list = cal_md5list(indexList=indexList,
                              srcfileKey=srcfile["Key"],
                              ChunkSize=ChunkSize_auto)
    # 计算所有分片列表的总etag: cal_etag
    digests = b"".join(m.digest() for m in md5list)
    md5full = hashlib.md5(digests)
    cal_etag = '"%s-%s"' % (md5full.hexdigest(), len(md5list))
    etag = '"%s"' % (md5full.hexdigest())
    return cal_etag, etag


# convert bytes to human readable string
def size_to_str(size):
    def loop(integer, remainder, level):
        if integer >= 1024:
            remainder = integer % 1024
            integer //= 1024
            level += 1
            return loop(integer, remainder, level)
        else:
            return integer, round(remainder / 1024, 1), level

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    integer, remainder, level = loop(int(size), 0, 0)
    if level + 1 > len(units):
        level = -1
    return f'{integer + remainder} {units[level]}'


# 本地文件重新计算一次MD5
def cal_md5list(*, indexList, srcfileKey, ChunkSize):
    logger.info(f'Re-read local file to calculate MD5 again: {srcfileKey}')
    md5list = []
    with open(os.path.join(SrcDir, srcfileKey), 'rb') as data:
        for partStartIndex in indexList:
            data.seek(partStartIndex)
            chunkdata = data.read(ChunkSize)
            chunkdata_md5 = hashlib.md5(chunkdata)
            md5list.append(chunkdata_md5)
    return md5list


# Single Thread Upload one part, from local to s3
def uploadThread(*, uploadId, partnumber, partStartIndex, srcfileKey, total, md5list, dryrun, complete_list, ChunkSize):
    prefix_and_key = str(PurePosixPath(S3Prefix) / srcfileKey)
    if not dryrun:
        print(f'\033[0;32;1m--->Uploading\033[0m {srcfileKey} - {partnumber}/{total}')
    pstart_time = time.time()
    with open(os.path.join(SrcDir, srcfileKey), 'rb') as data:
        retryTime = 0
        while retryTime <= MaxRetry:
            try:
                data.seek(partStartIndex)
                chunkdata = data.read(ChunkSize)
                chunkdata_md5 = hashlib.md5(chunkdata)
                md5list[partnumber - 1] = chunkdata_md5
                if not dryrun:
                    s3_dest_client.upload_part(
                        Body=chunkdata,
                        Bucket=DesBucket,
                        Key=prefix_and_key,
                        PartNumber=partnumber,
                        UploadId=uploadId,
                        ContentMD5=base64.b64encode(chunkdata_md5.digest()).decode('utf-8')
                    )
                    # 这里对单个part上传做了 MD5 校验，后面多part合并的时候会再做一次整个文件的
                break
            except Exception as err:
                retryTime += 1
                logger.info(f'UploadThreadFunc log: {srcfileKey} - {str(err)}')
                logger.info(f'Upload Fail - {srcfileKey} - Retry part - {partnumber} - Attempt - {retryTime}')
                if retryTime > MaxRetry:
                    logger.error(f'Quit for Max retries: {retryTime}')
                    input('PRESS ENTER TO QUIT')
                    sys.exit(0)
                time.sleep(5 * retryTime)  # 递增延迟重试
    complete_list.append(partnumber)
    pload_time = time.time() - pstart_time
    pload_bytes = len(chunkdata)
    pload_speed = size_to_str(int(pload_bytes / pload_time)) + "/s"
    if not dryrun:
        print(f'\033[0;34;1m    --->Complete\033[0m {srcfileKey} '
              f'- {partnumber}/{total} \033[0;34;1m{len(complete_list) / total:.2%} - {pload_speed}\033[0m')
    return


# Complete multipart upload, get uploadedListParts from S3 and construct completeStructJSON
def completeUpload(*, reponse_uploadId, srcfileKey, len_indexList, upload_etag_full):
    # 查询S3的所有Part列表uploadedListParts构建completeStructJSON
    prefix_and_key = srcfileKey
    if JobType == 'LOCAL_TO_S3':
        prefix_and_key = str(PurePosixPath(S3Prefix) / srcfileKey)
    uploadedListPartsClean = []
    PartNumberMarker = 0
    IsTruncated = True
    while IsTruncated:
        response_uploadedList = s3_dest_client.list_parts(
            Bucket=DesBucket,
            Key=prefix_and_key,
            UploadId=reponse_uploadId,
            MaxParts=1000,
            PartNumberMarker=PartNumberMarker
        )
        # NextPartNumberMarker = response_uploadedList['NextPartNumberMarker']
        IsTruncated = response_uploadedList['IsTruncated']

        if not IsTruncated:
            NextPartNumberMarker = 1

        if NextPartNumberMarker > 0:
            for partObject in response_uploadedList["Parts"]:
                ETag = upload_etag_full
                PartNumber = partObject["PartNumber"]
                NextPartNumberMarker = PartNumber
                addup = {
                    "ETag": ETag,
                    "PartNumber": PartNumber
                }
                uploadedListPartsClean.append(addup)
        PartNumberMarker = NextPartNumberMarker
    if len(uploadedListPartsClean) != len_indexList:
        logger.warning(f'Uploaded parts size not match - {srcfileKey}')
        sys.exit(0)
    completeStructJSON = {"Parts": uploadedListPartsClean}

    # S3合并multipart upload任务
    try:
        response_complete = s3_dest_client.complete_multipart_upload(
            Bucket=DesBucket,
            Key=prefix_and_key,
            UploadId=reponse_uploadId,
            MultipartUpload=completeStructJSON
        )
    except Exception as e:
        logger.error(f'complete_multipart_upload {DesBucket}/{prefix_and_key}, {str(e)}')
        sys.exit(0)
    logger.info(f'Complete merge file {srcfileKey}')
    return response_complete


# Compare local file list and s3 list
def compare_local_to_s3():
    logger.info('Comparing destination and source ...')
    fileList = get_local_file_list(str_key=True)
    desFilelist = get_s3_file_list(s3_client=s3_dest_client,
                                   bucket=DesBucket,
                                   S3Prefix=S3Prefix,
                                   no_prefix=True)
    deltaList = []
    for source_file in fileList:
        source_file["Key"] = str(PurePosixPath(source_file["Key"]))
        if source_file not in desFilelist:
            deltaList.append(source_file)

    if not deltaList:
        logger.warning('All source files are in destination Bucket/Prefix. Job well done.')
    else:
        logger.warning(f'There are {len(deltaList)} files not in destination or not the same size. List:')
        for delta_file in deltaList:
            logger.warning(str(delta_file))
    return


def s3_tool_upload(
        desBucket,
        s3Prefix,
        srcFileIndex,
        srcDir
):
    global logger, s3_dest_client
    start_time = datetime.datetime.now()
    ChunkSize_default = set_config(
        desBucket,
        s3Prefix,
        srcFileIndex,
        srcDir
    )
    logger, log_file_name = set_log()

    # Define s3 client
    s3_config = Config(max_pool_connections=200)
    s3_dest_client = Session(aws_access_key_id='root',
                             aws_secret_access_key='CBF5CCEC7425C19221F00D6A03B43B08').client('s3',
                                                                                              config=s3_config,
                                                                                              use_ssl=False,
                                                                                              endpoint_url=des_endpoint_url)
    # Check destination S3 writable
    try:
        logger.info(f'Checking write permission for: {DesBucket}')
        s3_dest_client.put_object(
            Bucket=DesBucket,
            Key=str(PurePosixPath(S3Prefix) / 'access_test'),
            Body='access_test_content'
        )
    except Exception as e:
        logger.error(f'Can not write to {DesBucket}/{S3Prefix}, {str(e)}')
        input('PRESS ENTER TO QUIT')
        sys.exit(0)

    # 获取源文件列表
    logger.info('Get source file list')
    src_file_list = []

    srcDir = str(Path(srcDir))
    src_file_list = get_local_file_list()

    # 获取目标s3现存文件列表
    des_file_list = get_s3_file_list(s3_client=s3_dest_client,
                                     bucket=DesBucket,
                                     S3Prefix=S3Prefix)

    # 获取Bucket中所有未完成的Multipart Upload
    multipart_uploaded_list = get_uploaded_list(s3_dest_client)

    # 对文件列表中的逐个文件进行上传操作
    with futures.ThreadPoolExecutor(max_workers=MaxParallelFile) as file_pool:
        for src_file in src_file_list:
            file_pool.submit(upload_file,
                             srcfile=src_file,
                             desFilelist=des_file_list,
                             UploadIdList=multipart_uploaded_list,
                             ChunkSize_default=ChunkSize_default)

    # 再次获取源文件列表和目标文件夹现存文件列表进行比较，每个文件大小一致，输出比较结果
    time_str = str(datetime.datetime.now() - start_time)

    str_from = f'{srcDir}'
    compare_local_to_s3()

    print(f'\033[0;34;1mMISSION ACCOMPLISHED - Time: {time_str} \033[0m - FROM: {str_from} TO {DesBucket}/{S3Prefix}')
    print('Logged to file:', os.path.abspath(log_file_name))
