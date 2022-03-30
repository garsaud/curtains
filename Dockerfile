FROM python:alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir fauxmo

RUN apk add gcc musl-dev
RUN pip install --no-cache-dir RPi.GPIO

COPY config.json ./
COPY src ./src

CMD [ "fauxmo", "-c", "config.json", "-v" ]
