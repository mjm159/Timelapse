# Standard Library
from configparser import ConfigParser
import logging
import os
import sys

# 3rd Party Modules
import boto3
from botocore.exceptions import ClientError


# Setting up config parser
parser = ConfigParser()
parser.read('uploader.ini')

# Basic globals
logging.basicConfig(filename='logs/upload_to_bucket.log', filemode='w', format='%(asctime)s - %(levelname) - %(message)s')
BUCKET = parser.get('uploader', 'bucket')
FOLDER = parser.get('uploader', 'folder')


class TooFewCommandLineArgumentsException(Exception):
    pass


def upload_image(bucket: str, filepath: str, object_name: str, folder: str = None) -> bool:
    """
    Uploads file to a bucket in in S3 and to a specific folder if provided

    :param bucket: destination bucket in S3
    :param filepath: path to file to upload
    :param object_name: indicates what name to store the object with in S3
    :param folder: if set indicates folder in S3 bucket to put object into
    :return: True if file upload was successful, else False
    """
    # Adding folder if present
    if folder:
        object_name = f'{folder}/{object_name}'
    # Upload to S3
    s3_client = boto3.client('s3')
    try:
        logging.info(f'Uploading {filepath}')
        response = s3_client.upload_file(filepath, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def clean_up(filepath: str) -> bool:
    """
    Removes file at filepath
    :param filepath: path of file to remove
    :return: True if successful, else False
    """
    if os.path.exists(filepath):
        logging.info(f'Removing {filepath}')
        os.remove(filepath)
        return True
    return False


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        raise TooFewCommandLineArgumentsException
    filepath = args[1]
    filename = args[2]
    successful_upload = upload_image(bucket=BUCKET,
                                     filepath=filepath,
                                     object_name=filename,
                                     folder=FOLDER)
    if successful_upload:
        clean_up(filepath)
