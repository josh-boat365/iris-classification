FROM ubuntu:latest

RUN apt-get upgrade -y
RUN apt-get install -y python3-pip python3-dev build-essaential

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "appy.py" ]