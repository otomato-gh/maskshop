1. Please add a .dockerignore file to exclude README.md from docker builds

2. Please add a Dockerfile for the application image:

- based on python:alpine
- set working directory to /app
- copy all files to /app directory
- move settings.prod.py to settgins.py
- install dependencies by running `pip install -r requirements.txt`
- set environment variable INITDB to `true`
- create user 'appuser' (adduser -D appuser)
- make appuser the owner of '/app' (`chown -R appuser:appuser /app`)
- switch the image to run as 'appuser'
- specify that port 80 will be exposed
- set the default command to `python front.py`
