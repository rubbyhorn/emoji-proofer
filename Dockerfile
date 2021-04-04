FROM python:3.8.8-alpine3.13

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY app /app

CMD python3 app/__init__.py
