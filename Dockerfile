#Activity 2.4 Docker File 
# syntax=docker/dockerfile:1

FROM python:3.10

COPY ./ /var

WORKDIR /var

RUN python -m pip install -r requirements.txt

ENV FLASK_APP=hello.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

##Added some new

EXPOSE 5001

RUN apt-get update 

RUN apt-get -y install gcc

COPY . .






######################################################### Old  ##########################################

#FROM python:3.9-slim

#WORKDIR /app

#COPY requirements.txt requirements.txt

#RUN apt-get update 

#RUN apt-get -y install gcc

#RUN pip3 install -r requirements.txt

#COPY . .

#ENV FLASK_APP=hello.py

#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

