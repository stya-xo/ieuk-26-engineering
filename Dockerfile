FROM python:3-slim

WORKDIR /app

RUN pip install pandas

COPY . /app

CMD [ "python", "./main.py" ]