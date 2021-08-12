import ipaddress

from m3ta import getIP

networkInfo = """SSID:	ZAP-35A0
Protocol:	Wi-Fi 4 (802.11n)
Security type:	WPA2-Personal
Network band:	2.4 GHz
Network channel:	11
Link-local IPv6 address:	fe80::5804:e955:eb67:c59a%5
IPv4 address:	192.168.1.12
IPv4 DNS servers:	192.168.1.1
Manufacturer:	Ralink Technology, Corp.
Description:	Ralink RT5390R 802.11bgn Wi-Fi Adapter
Driver version:	5.0.57.1
Physical address (MAC):	A4-17-31-AB-F1-65
"""
# print(networkInfo.splitlines())

info = {i.split(":\t")[0]:i.split(":\t")[1] for i in networkInfo.splitlines()}
# print(info['IPv4 DNS servers'])

networkAddress = info['IPv4 DNS servers']

self = lambda: ipaddress.ip_address(getIP())
# print(self(),self().version,sep='\n',end='\n\n')
# host = 
print(self().host)

host = ipaddress.ip_interface(networkAddress)
net = ipaddress.ip_network(host)
print(host.network,net,net.num_addresses,sep='\n',end='\n\n')