FROM python:3.10
WORKDIR /proj
COPY ./requirements.txt requirements.txt 
RUN python3.10 -m pip install -r requirements.txt
COPY ./ ./