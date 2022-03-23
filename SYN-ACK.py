#!/usr/bin/python
# Import scapy
from scapy.all import *
import sys

# arg = sys.argv[1]
#print(sys.argv[0])

# Print info header
# print "[*] TCP Handshake example -- Thijs 'Thice' Bosschert, 06-06-2011"
# print('hello')
# Set up target IP
# ip=IP(src = "10.0.0.2",dst="10.0.0.1")
ip=IP(src = "10.0.0.2",dst=str(sys.argv[1]))

# Generate random source port number
# port=RandNum(1024,65535)
port = 8000
#Ether(src="ab:cd:ef:ab:cd:ef", dst="ff:ff:ff:ff:ff:ff")/IP(src="1.2.3.4", dst="3.4.5.6")
SYNACK = Ether(src="9e:e2:d1:4f:ca:c0", dst=sys.argv[2])/ip/TCP(sport=port,dport = int(sys.argv[3]),flags = "SA",seq =0,ack = 1000)
sendp(SYNACK,  iface='s1-eth1')
# send(SYNACK)
