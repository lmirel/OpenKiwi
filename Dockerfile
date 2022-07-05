FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL /bin/bash
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

ARG WORKSPACE=/OpenKiwi

WORKDIR ${WORKSPACE}

RUN apt update && apt --yes --force-yes install wget unzip python3 python3-pip python3-dev virtualenv
RUN pip3 install openkiwi==2.1.0
RUN wget https://github.com/lmirel/OpenKiwi/archive/refs/heads/predict-enzh.zip && unzip predict-enzh.zip

#RUN cd OpenKiwi-2.1.0/ && \
#    wget https://github.com/lmirel/OpenKiwi/releases/download/2.1.0/xlmr-en-zh.ckpt

RUN apt -y autoremove && apt clean && rm -rf /var/lib/apt/lists/*

CMD cd OpenKiwi-predict-enzh/ && \
    PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python python3 predict_enzh.py
    #/bin/bash
