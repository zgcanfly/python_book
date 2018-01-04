FROM python:3.6.1
MAINTAINER zgyang
WORKDIR /usr/src
USER root
COPY  . /usr/src/
CMD ["pip","install -r requirements.txt"]
