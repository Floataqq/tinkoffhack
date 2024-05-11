FROM mongo:latest

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get -y install python3 && \ 
    mongod & disown && \            # start mongodb

