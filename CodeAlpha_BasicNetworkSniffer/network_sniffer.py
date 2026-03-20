from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        print("\n==============================")
        print("Packet Captured")
        print("==============================")
        print(f"Source IP       : {ip_layer.src}")
        print(f"Destination IP  : {ip_layer.dst}")

        if packet.haslayer(TCP):
            print("Protocol        : TCP")
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print("Protocol        : UDP")
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        else:
            print("Protocol        : Other")

print("Starting Network Sniffer...")
sniff(prn=process_packet, store=False)