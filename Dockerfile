FROM python:3.8

# pipのアップグレード
RUN pip install --upgrade pip

# PyGObjectのビルドに必要なライブラリをインストールする
# RUN apt-get update && apt-get install -y libgirepository1.0-dev libcairo2-dev

RUN pip install Cython
# Cコンパイラ
#RUN apt-get update && apt-get install -y build-essential
# dbus-python
#RUN apt-get update && apt-get install -y libdbus-1-dev
# pycups
#RUN apt-get update && apt-get install -y libcups2-dev

# Pythonの開発ツールもインストール
#RUN apt-get update && apt-get install -y python3-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
