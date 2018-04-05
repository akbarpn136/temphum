FROM python:3.5
LABEL author="akbarpn136"

RUN apt-get update && \
    apt-get -y install python3-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade pip && \
    pip3 install falcon && \
    pip3 install falcon-cors && \
    pip3 install gevent && \
    pip3 install gunicorn && \
    pip3 install kafka-python

RUN mkdir /var/www && \
    mkdir /var/www/temphum

WORKDIR /var/www/temphum
COPY . .
EXPOSE 8000