FROM python:3.6.1
MAINTAINER zgyang
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

