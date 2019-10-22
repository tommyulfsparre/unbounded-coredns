FROM tcely/powerdns-server

RUN apk update && apk add -u python bind-tools

COPY slow-pipe.py /usr/local/bin/slow-pipe.py
COPY pdns.conf /etc/pdns/pdns.conf
EXPOSE 2053/tcp 2053/udp

ENTRYPOINT ["/usr/local/sbin/pdns_server", "--disable-syslog"]