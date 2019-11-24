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

## Instructions

## Credit
A special thanks to Caroline Dunn who's tutorial let me to build this in the first place [link](https://www.youtube.com/watch?v=ofKqZx4DIhM)

## Sources
- [YouTube - Timelapse Raspberry Pi Tutorial](https://www.youtube.com/watch?v=ofKqZx4DIhM)
- [Raspberry Pi Foundation - Using a Webcam](https://www.raspberrypi.org/documentation/usage/webcams/)
- [Using SCP](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
