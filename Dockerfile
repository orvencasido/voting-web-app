FROM ubuntu:22.04

RUN apt update && apt install -y python3-pip python3-dev redis-server curl

COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY app /app
WORKDIR /app

CMD ["python3", "main.py"]
