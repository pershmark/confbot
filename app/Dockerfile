FROM python:3.8

RUN apt-get update
RUN apt-get install git

WORKDIR /srv/project

COPY ./ ./
COPY ./requirements.txt ./


RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]
