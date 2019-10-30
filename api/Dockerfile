
FROM ubuntu

WORKDIR /app

RUN apt update && apt install -y \
    python3-pip

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt

COPY . /app

CMD ["python3", "/app/app.py"]

