from scapy.all import sniff
import pandas as pd

packet_data = []

protocol_map = {
    6: "TCP",
    17: "UDP",
    1: "ICMP"
}

def process_packet(packet):
    try:
        if packet.haslayer("IP"):
            src_ip = packet["IP"].src
            dst_ip = packet["IP"].dst
            proto = packet["IP"].proto
            protocol = protocol_map.get(proto, str(proto))
            length = len(packet)
            
            port = packet.sport if packet.haslayer("TCP") or packet.haslayer("UDP") else 0
            
            packet_data.append([src_ip, dst_ip, protocol, length, port])
    except Exception:
        pass

def capture_packets():
    global packet_data
    packet_data = []

    sniff(prn=process_packet, count=50)

    df = pd.DataFrame(packet_data, columns=["Source IP", "Destination IP", "Protocol", "Length", "Port"])
    df.to_csv("logs.csv", index=False)

    return df