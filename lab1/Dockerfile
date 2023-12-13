FROM alpine:3.18

LABEL maintainer="Aleksandr Gerasimov"

COPY . ./workdir

COPY index.html /usr/share/nginx/html/index.html

RUN apk update && \
    apk upgrade && \
    apk add bash nginx openrc

RUN mv workdir/nginx.conf /etc/nginx/nginx.conf

# RUN apk update && \
#     apk upgrade && \
#     apk add bash nginx && \
#     adduser -D -g 'www' www && \
#     mkdir /www && \
#     chown -R www:www /var/lib/nginx && \
#     chown -R www:www /www && \
#     mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig && \
#     apk add openrc --no-cache && \
#     sh workdir/setup.sh

EXPOSE 80/tcp

CMD ["sh", "workdir/run.sh"]
