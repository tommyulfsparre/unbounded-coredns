FROM debian:stretch-slim as builder

RUN apt-get update -y && apt-get install -y curl libbind-dev libkrb5-dev libssl-dev libcap-dev libxml2-dev libjson-c-dev libgeoip-dev build-essential pkg-config
RUN curl -sL https://www.dns-oarc.net/files/dnsperf/dnsperf-2.3.2.tar.gz -o /tmp/dnsperf-2.3.2.tar.gz
RUN cd /tmp && tar zxvf dnsperf-2.3.2.tar.gz
RUN cd /tmp/dnsperf-2.3.2 && ./configure && make && make install

FROM debian:stretch-slim  
WORKDIR /tmp
RUN apt-get update -y && apt-get install -y libbind-dev libssl-dev
COPY queryfile /tmp/queryfile
COPY --from=builder /usr/local/bin/dnsperf /usr/local/bin/dnsperf
CMD ["/usr/local/bin/dnsperf"]  
