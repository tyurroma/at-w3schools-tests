FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .

RUN apt update; apt install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm -rf google-chrome-stable_current_amd64.deb && \
    pip3 --no-cache-dir install -r requirements.txt

COPY . .
EXPOSE 9000/tcp
ENTRYPOINT ["/app/run.sh"]