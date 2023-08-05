import time

import download
import upload

if __name__ == '__main__':

    download.s3_tool_download(
        srcBucket="publish-data",
        s3Prefix="train_data/uie_pretrained_model/",
        srcFileIndex="model_epoch=09.ckpt",
        desDir="/tmp")

    # srcBucket
    # 源Bucket
    #
    # s3Prefix
    # 源Bucket的Prefix
    #
    # srcFileIndex
    # 指定下载文件的文件名, 全部文件则用 "*"
    #
    # desDir = /Users/testUser/Documents
    # 文件本地存放目录

    time.sleep(5)
    upload.s3_tool_upload(
        desBucket='archives',
        s3Prefix='',
        srcFileIndex='model_epoch=09.ckpt',
        srcDir='/tmp/train_data/uie_pretrained_model/')
    # desBucket = myBucket
    # Destination S3 bucket name
    # 目标文件bucket, type = str

    # s3Prefix =
    # S3_TO_S3 mode Src. S3 Prefix, and same as Des. S3 Prefix; LOCAL_TO_S3 mode, this is Des. S3 Prefix.
    # 目标S3的Prefix, type = str

    # srcFileIndex = *
    # Specify the file name to upload. Wildcard "*" to upload all.
    # 指定要上传的文件的文件名, type = str，Upload全部文件则用 "*"

    # srcDir = '/tmp/train_data/uie_pretrained_model/'
    # Source file directory. It is useless in S3_TO_S3 mode
    # 原文件本地存放目录 type = str
    print("end !")
