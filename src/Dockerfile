FROM ubuntu:14.04
MAINTAINER Rafael D Santos "santosdrafael@gmail.com"
RUN apt-get update && apt-get install -y wget
RUN wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add -
RUN echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list
RUN apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    curl \
    openjdk-7-jdk
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 webservice.py

