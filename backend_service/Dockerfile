FROM python:2.7.10  

WORKDIR /backend

ADD . /backend

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]