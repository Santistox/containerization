FROM alpine:3.18

LABEL maintainer="Aleksandr Gerasimov"

COPY . ./workdir

COPY index.html /usr/share/nginx/html/index.html

RUN apk update && \
    apk upgrade && \
    apk add bash nginx openrc

RUN apk -v cache clean

RUN mv workdir/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80/tcp

CMD ["sh", "workdir/run.sh"]
