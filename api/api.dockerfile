FROM python:3.11-slim-buster

WORKDIR /api
RUN mkdir log
COPY requirements.txt /api
RUN pip3 install -r requirements.txt

ADD . /api

RUN chmod +x /api/run.sh

EXPOSE 8000

CMD ["/api/run.sh"]