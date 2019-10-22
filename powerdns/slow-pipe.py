#!/usr/bin/python -u

import time
from sys import stdin, stdout, stderr


def run():
    data = stdin.readline()
    stdout.write("OK\tDumb pipe\n")
    stdout.flush()

    while True:
        data = stdin.readline().strip()
        stderr.write(data + "\n")
        kind, qname, qclass, qtype, id, ip = data.split("\t")

        if (qtype == "SOA"):
            response = "DATA\t{qname}\t{qclass}\tSOA\t86400\t-1\t pdns.example.com\t hostmaster.example.com\t 123456 1800 3600 604800 3600\n".format(
                qname=qname,
                qclass=qclass)
            stdout.write(response)

        if (qname.startswith('ip-') and qtype == "ANY"): 
            parts = qname.split('.')
            ip = parts[0].split('ip-')[1].replace('-', '.')

            response = "DATA\t{qname}\t{qclass}\tA\t{ttl}\t-1\t{ip}\n".format(
                qname=qname,
                qclass=qclass,
                ttl=60,
                ip=ip)

            stderr.write(response)
            stdout.write(response)     

        stdout.write("END\n")
        stdout.flush()

if __name__ == "__main__":
    run()