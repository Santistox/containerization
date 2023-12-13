FROM alpine:3.18

LABEL maintainer="Aleksandr Gerasimov"

RUN apk update && apk upgrade && apk add bash

COPY . ./workdir

CMD ["./setup.py"]
