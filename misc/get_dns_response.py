from scapy.all import *

url_in = raw_input("Put a url: ") 
dns_req = IP(dst = "8.8.8.8")/UDP(dport = 53)/DNS(rd = 1, qd = DNSQR(qname = url_in))
res = sr1(dns_req, verbose = 0)

print(res[DNS].show())

