# -*- coding: utf-8 -*-
# PROJECT LONGBOW - AMAZON S3 DOWNLOAD TOOL WITH BREAK-POINT RESUMING
import os
import sys
import json
from boto3.session import Session
from botocore.client import Config
from concurrent import futures
import uuid
import datetime
import logging
from pathlib import PurePosixPath, Path
import sqlite3
import time

os.system("")

global SrcBucket, S3Prefix, SrcFileIndex, SrcProfileName, DesDir, MaxRetry, MaxThread, MaxParallelFile, LoggingLevel, endpoint_url, logger, s3_src_client
max_get = 1000


# Read config.ini with GUI
def set_config(srcBucket, s3Prefix, srcFileIndex, desDir):
    global SrcBucket, S3Prefix, SrcFileIndex, SrcProfileName, DesDir, MaxRetry, MaxThread, MaxParallelFile, LoggingLevel, endpoint_url
    endpoint_url = "http://172.16.10.19:39999/api/v1/s3"
    SrcBucket = srcBucket
    S3Prefix = s3Prefix
    SrcFileIndex = srcFileIndex
    DesDir = desDir
    Megabytes = 1024 * 1024
    ChunkSize = 500 * Megabytes
    MaxRetry = 5
    MaxThread = 5
    MaxParallelFile = 5
    LoggingLevel = 'INFO'
    if S3Prefix == '/':
        S3Prefix = ''
    return ChunkSize


# Configure logging
def set_log():
    logger = logging.getLogger()
    # File logging
    if not os.path.exists("./log"):
        os.mkdir("log")
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


# Get object list on S3
def get_s3_file_list(s3_client, bucket):
    logger.info('Get s3 file list ' + bucket)
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


# Check single file on S3
def head_s3_single_file(s3_client, bucket):
    try:
        response_fileList = s3_client.head_object(
            Bucket=bucket,
            Key=str(PurePosixPath(S3Prefix) / SrcFileIndex)
        )
        file = [{
            "Key": str(PurePosixPath(S3Prefix) / SrcFileIndex),
            "Size": response_fileList["ContentLength"]
        }]
    except Exception as err:
        logger.error(str(err))
        input('PRESS ENTER TO QUIT')
        sys.exit(0)
    return file


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


def download_thread(partnumber, partStartIndex, srcfileKey, total, complete_list, ChunkSize, wfile):
    try:
        logger.info(f'Downloading {srcfileKey} - {partnumber}/{total}')
        pstart_time = time.time()
        response_get_object = s3_src_client.get_object(
            Bucket=SrcBucket,
            Key=srcfileKey,
            Range="bytes=" + str(partStartIndex) + "-" + str(partStartIndex + ChunkSize - 1)
        )
        getBody = response_get_object["Body"].read()
        complete_list.append(partnumber)
        pload_time = time.time() - pstart_time
        pload_bytes = len(getBody)
        pload_speed = size_to_str(int(pload_bytes/pload_time)) + "/s"
        # 写入文件
        wfile.seek(partStartIndex)
        wfile.write(getBody)
        print(f'\033[0;34;1m --->Complete\033[0m {srcfileKey} '
              f'- {partnumber}/{total}\033[0;34;1m {len(complete_list) / total:.2%} - {pload_speed}\033[0m')

        # 写入partnumber数据库
        dir_and_key = Path(DesDir) / srcfileKey
        try:
            with sqlite3.connect('s3_download.db') as db:
                cursor = db.cursor()
                uuid1 = uuid.uuid1()
                cursor.execute(f"INSERT INTO S3P (ID, BUCKET, KEY, PARTNUMBER) "
                               f"VALUES ('{uuid1}', '{SrcBucket}', '{dir_and_key.as_uri()}', {partnumber})")
                db.commit()
                logger.info(f'Download part completed. Write to DB {srcfileKey} - {partnumber}/{total}')
        except Exception as e:
            logger.warning(f'Fail to insert DB: {dir_and_key.as_uri()}, {str(e)}')
    except Exception as e:
        logger.warning(f'Fail to download {srcfileKey} - {partnumber}/{total}. {str(e)}')
    return


def download_part(indexList, partnumberList, srcfile, ChunkSize_auto, wfile):
    partnumber = 1  # 当前循环要上传的Partnumber
    total = len(indexList)
    complete_list = []
    # 线程池Start
    with futures.ThreadPoolExecutor(max_workers=MaxThread) as pool:
        for partStartIndex in indexList:
            # start to download part
            if partnumber not in partnumberList:
                pool.submit(download_thread, partnumber, partStartIndex, srcfile["Key"], total,
                            complete_list, ChunkSize_auto, wfile)
            else:
                complete_list.append(partnumber)
            partnumber += 1
    # 线程池End
    logger.info(f'All parts downloaded - {srcfile["Key"]} - size: {srcfile["Size"]}')
    return


# 创建文件目录结构
def create_dir(file_dir):
    parent = file_dir.parent
    if not Path.exists(parent):
        create_dir(parent)
    try:
        Path.mkdir(file_dir)
    except Exception as e:
        logger.error(f'Fail to mkdir {str(e)}')


# Download file
def download_file(srcfile, ChunkSize_default):
    logger.info(f'Start file: {srcfile["Key"]}')
    dir_and_key = Path(DesDir) / srcfile["Key"]
    if Path.exists(dir_and_key):
        if dir_and_key.stat().st_size == srcfile["Size"] or dir_and_key.is_dir():
            logger.info(f'Duplicated: {dir_and_key.as_uri()} same size, goto next file.')
            return

    # 创建文件目录结构
    path = dir_and_key.parent
    if not Path.exists(path):
        create_dir(path)

    # 如果是子目录就跳过下载
    if srcfile["Key"][-1] == '/':
        Path.mkdir(dir_and_key)
        logger.info(f'Create empty subfolder: {dir_and_key.as_uri()}')
        return

    # 获取已下载的 part number list
    partnumberList = []
    try:
        with sqlite3.connect('s3_download.db') as db:
            cursor = db.cursor()
            p_sql = cursor.execute(f"SELECT PARTNUMBER FROM S3P WHERE BUCKET='{SrcBucket}' AND KEY='{dir_and_key.as_uri()}'")
            db.commit()
            partnumberList = [d[0] for d in p_sql]
            logger.info(f'Got partnumberList {dir_and_key.as_uri()} - {json.dumps(partnumberList)}')
    except Exception as e:
        logger.error(f'Fail to select partnumber from DB. {str(e)}')

    # 获取索引列表，例如[0, 10, 20]
    indexList, ChunkSize_auto = split(srcfile, ChunkSize_default)

    # 执行download
    s3tmp_name = dir_and_key.with_suffix('.s3tmp')
    if Path.exists(s3tmp_name):
        mode = 'r+b'
    else:
        # 如果没有临时文件，或被删除了，则新建文件并将partnumberList清空
        mode = 'wb'
        partnumberList = []
    with open(s3tmp_name, mode) as wfile:
        download_part(indexList, partnumberList, srcfile, ChunkSize_auto, wfile)

    # 修改文件名.s3part，清理partnumber数据库
    s3tmp_name.rename(dir_and_key)
    try:
        with sqlite3.connect('s3_download.db') as db:
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM S3P WHERE BUCKET='{SrcBucket}' AND KEY='{dir_and_key.as_uri()}'")
            db.commit()
    except Exception as e:
        logger.warning(f'Fail to clean DB: {dir_and_key.as_uri()}. {str(e)}')
    logger.info(f'Finsh: {srcfile["Key"]} TO {dir_and_key.as_uri()}')
    return


# Compare local file list and s3 list
def compare_local_to_s3():
    logger.info('Comparing destination and source ...')
    if SrcFileIndex == "*":
        s3Filelist = get_s3_file_list(s3_src_client, SrcBucket)
    else:
        s3Filelist = head_s3_single_file(s3_src_client, SrcBucket)
    deltaList = []

    for srcfile in s3Filelist:
        dir_and_key = Path(DesDir) / srcfile["Key"]
        # 文件不存在
        if not Path.exists(dir_and_key):
            deltaList.append(srcfile)
            continue
        # 文件大小
        if srcfile["Key"][-1] != '/':
            if srcfile["Size"] != dir_and_key.stat().st_size:
                deltaList.append(srcfile)
                continue

    if not deltaList:
        logger.info('All source files are in destination, job well done.')
    else:
        logger.warning(f'There are {len(deltaList)} files not in destination or not the same size. List:')
        logger.warning(str(deltaList))
    return


# Main
def s3_tool_download(
        srcBucket,
        s3Prefix,
        srcFileIndex,
        desDir):
    start_time = datetime.datetime.now()
    ChunkSize_default = set_config(srcBucket, s3Prefix, srcFileIndex, desDir)
    global logger, s3_src_client
    logger, log_file_name = set_log()

    # Define s3 client
    s3_config = Config(max_pool_connections=200, retries={'max_attempts': MaxRetry})
    s3_src_client = Session(aws_access_key_id='root',
                            aws_secret_access_key='CBF5CCEC7425C19221F00D6A03B43B08').client('s3',
                                                                                             config=s3_config,
                                                                                             use_ssl=False,
                                                                                             endpoint_url=endpoint_url)

    # Define DB table
    with sqlite3.connect('s3_download.db') as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS S3P "
                       "(ID TEXT PRIMARY KEY, "
                       "BUCKET TEXT, "
                       "KEY TEXT, "
                       "PARTNUMBER INTEGER)")
        db.commit()

    # 获取源文件列表
    logger.info('Get source file list')
    if SrcFileIndex == "*":
        src_file_list = get_s3_file_list(s3_src_client, SrcBucket)
    else:
        src_file_list = head_s3_single_file(s3_src_client, SrcBucket)

    # 对文件列表中的逐个文件进行下载操作
    with futures.ThreadPoolExecutor(max_workers=MaxParallelFile) as file_pool:
        for src_file in src_file_list:
            file_pool.submit(download_file, src_file, ChunkSize_default)

    # 再次获取源文件列表和目标文件夹现存文件列表进行比较，每个文件大小一致，输出比较结果
    time_str = str(datetime.datetime.now() - start_time)
    compare_local_to_s3()
    print(f'\033[0;34;1mMISSION ACCOMPLISHED - Time: {time_str} \033[0m - FROM: {SrcBucket}/{S3Prefix} TO {DesDir}')
    print('Logged to file:', os.path.abspath(log_file_name))
