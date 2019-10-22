FROM coredns/coredns

COPY corefile /etc/coredns/corefile
EXPOSE 1053/tcp 1053/udp

ENTRYPOINT ["./coredns", "-dns.port=1053", "-conf=/etc/coredns/corefile"]