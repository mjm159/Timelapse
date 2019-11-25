#!/bin/bash

# Capture photo
RESOLUTION="1920x1080"
HOSTNAME=$(uname -n)
DATE=$(date +"%Y-%m-%d_%H-%M-%S_%Z")
IMAGE_PATH=$(cd ~;pwd)/images
IMG_FILENAME=$HOSTNAME\_$DATE.jpg
IMG_FILEPATH=$IMAGE_PATH/$IMG_FILENAME
fswebcam -r $RESOLUTION --no-banner $IMG_FILEPATH

# Upload
source /home/michael/Timelapse/env/bin/activate
python3 /home/michael/Timelapse/upload_to_bucket.py $IMG_FILEPATH $IMG_FILENAME
