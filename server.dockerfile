FROM python:latest

WORKDIR /server-flask

RUN pip3 install flask

COPY server.py .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]