CoreDNS repro
---

# Setup 

Containers with a shared network namespace.
```
+------------------------------------------------------+
|                                                      |
| +-----------+      +-----------+      +-----------+  |
| |  dnsperf  |      |  coredns  |      | powerdns  |  |
| +-----------+      +-----------+      +-----------+  |
|      \--> 127.0.0.1:10553     \----> 127.0.0.1:2053  |
|                                                      |
+------------------------------------------------------+
```

## Build containers locally  
```bash
docker build -t dnsperf:repro -f dnsperf/Dockerfile dnsperf
docker build -t pdns-backend:repro -f powerdns/Dockerfile powerdns
docker build -t coredns:repro -f coredns/Dockerfile coredns
docker build -t coredns-limit:repro -f coredns-limit/Dockerfile coredns-limit
```

## Run with coredns/coredns:latest 
```bash
docker run -it --rm -p 1053:1053/tcp -p 1053:1053/udp -p 1180:1180/tcp --name coredns --memory=1024m coredns:repro
docker run -it --rm --name powerdns --memory=1024m --network=container:coredns pdns-backend:repro
```

run [dnsperf](#run-dnsperf).


## Run with CoreDNS master with limit plugin
```bash
docker run -it --rm -p 1053:1053/tcp -p 1053:1053/udp -p 1180:1180/tcp --name coredns --memory=1024m coredns-limit:repro
docker run -it --rm --name powerdns --memory=1024m --network=container:coredns pdns-backend:repro
```

run [dnsperf](#run-dnsperf).

## Run dnsperf
Send DNS request to 127.0.0.1:1053 acting as 100 client for 180 seconds with a 10 seconds query timeout and limit the number of outstanding request to 20000.

Use input file /tmp/queryfile. The queryfile is copied into the container and can be viewed [here](dnsperf/queryfile).

**It's important to increase the number of outstanding request for dnsperf, otherwise dnsperf will limit the concurrency.**

```bash
docker run -it --rm --name dnsperf --memory=256m --network=container:coredns dnsperf:repro /usr/local/bin/dnsperf -s 127.0.0.1 -p 1053 -c 100 -q 20000 -l 180 -t 10 -S 5 -T 4 -d /tmp/queryfile
```

## Graph with Prometheus 
The CoreDNS container will expose port 1180 for exposing metrics in the Prometheus exposition format. 

The included [prometheus.yaml](prometheus.yaml) can be used to run Prometheus locally to ingest the CoreDNS metrics.

