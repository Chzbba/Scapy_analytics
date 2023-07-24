from scapy.all import *
a = sniff(count = 100)  #Захват 100 пакетов трафика и помещение их в переменную 'a'
wrpcap("dump.pcap", a)
traffic = PcapReader("dump.pcap")   #Объект средства чтения файлов .pcap
for packet in traffic:
    print(packet.show())    #Вывод информации о каждом пакете