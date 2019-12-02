# Timelapse
A Raspberry Pi powered webcam taking timelapse photos

## Setup
- Pi environment
	- Assemble web cam & pi
	- install OS & configure
	- Create new user and change to user
	- setup ssh
	- setup environment
- S3
    - setup account
    - create bucket
    - create policy
    - create group & add appropriate policy
    - create users & add to appropriate group
    - Download user `credentials.csv`
    - create `images` folder
- boto3
    - sudo apt-get install -y python3
    - sudo apt-get install -y python3-pip
    - sudo apt-get install -y python3-venv
    - python3 -m venv env
    - source env/bin/activate
    - pip3 install awscli
    - aws configure
- Config garbage
    - make sure PATH is setup
    - crontab doesn't use environment variables, not even PATH
    - All filepaths need to be absolute
    - crontab -e
        - /6 * * * * /home/michael/Timelapse/capture_photo.sh >/dev/null 2>&1

## Instructions

## ToDo
- Find better system to manager filepath references

## Credit
A special thanks to Caroline Dunn who's tutorial let me to build this in the first place [link](https://www.youtube.com/watch?v=ofKqZx4DIhM)

## Sources
- [YouTube - Timelapse Raspberry Pi Tutorial](https://www.youtube.com/watch?v=ofKqZx4DIhM)
- [Raspberry Pi Foundation - Using a Webcam](https://www.raspberrypi.org/documentation/usage/webcams/)
- [Using SCP](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [strftime Formatting](http://man7.org/linux/man-pages/man3/strftime.3.html)
- [Config Parser](https://docs.python.org/3/library/configparser.html)
- [Python file manager](https://realpython.com/working-with-files-in-python/)
- [Python logging](https://realpython.com/python-logging/#basic-configurations)
- [Boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
    - [Example S3 uploading](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
    - [AWS Cli docs](https://aws.amazon.com/cli/)
- Crontab
    - [Quick Reference](https://www.adminschoice.com/crontab-quick-reference)
    

