FROM python:latest

WORKDIR /client-flask

COPY client.py .

CMD [ "python" , "client.py"]