FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /app
COPY app /app
RUN pip install spotipy
RUN pip install wikiapi
RUN pip install python-telegram-bot==6.1b0
RUN pip install urllib3==1.13.1
RUN pip install requests==2.9.1
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT wsgi 			