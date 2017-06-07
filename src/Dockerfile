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
    software-properties-common \
    openjdk-7-jdk
RUN \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
RUN wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
RUN echo 'deb http://debian.neo4j.org/repo stable/' | sudo tee -a /etc/apt/sources.list.d/neo4j.list
RUN sudo apt-get update
RUN apt-get install -y neo4j
RUN mkdir /var/run/neo4j && chown neo4j /var/run/neo4j
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN neo4j-admin set-initial-password pudim
RUN neo4j start
EXPOSE 5000 80
EXPOSE 7474 7473 7687
RUN chmod +x init_server.sh
CMD ./init_server.sh
