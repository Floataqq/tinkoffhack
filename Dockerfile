FROM mongo:latest

WORKDIR /app

COPY . .
COPY mongodb_entrypoint.js /docker-entrypoint-initdb.d

SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get -y install python3 python3-pip
RUN mongod & disown
RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "api.py" ]

