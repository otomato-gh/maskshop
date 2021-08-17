1. Please add a .dockerignore file to exclude README.md from docker builds

2. Please add a Dockerfile for the application image:

- based on `python:alpine`
- set working directory to /api
- copy all files to /api directory
- install dependencies by running  `pip install -r requirements.txt`
- create user 'appuser' (`adduser -D appuser`)
- make `appuser` the owner of '/api' (`chown -R appuser:appuser /api`)
- switch the image to run as 'appuser'
- specify that port 80 will be exposed
- set the default command to  `python api.py`
