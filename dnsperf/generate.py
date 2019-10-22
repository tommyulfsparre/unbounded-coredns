import random
import socket
import struct

f = open("queryfile", "a")

for x in xrange(0, 100000):
    ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    output = 'ip-{ip}.example.com.\tA\n'.format(ip=ip.replace('.', '-'))
    f.write(output)

f.close()