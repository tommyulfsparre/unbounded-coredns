FROM golang:1.13.2-stretch as builder

RUN apt-get update -y && apt-get install -y git
RUN git clone https://github.com/tommyulfsparre/coredns /tmp/coredns
RUN cd /tmp/coredns && git checkout max-inflight && make 

FROM debian:stretch-slim 
WORKDIR /tmp
COPY corefile /etc/coredns/corefile
COPY --from=builder /tmp/coredns/coredns /coredns

EXPOSE 1053/tcp 1053/udp
ENTRYPOINT ["/coredns", "-dns.port=1053", "-conf=/etc/coredns/corefile"]
