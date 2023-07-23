from scapy.all import *
a = sniff(count = 100)
wrpcap("dump.pcap", a)
print(a.nsummary())