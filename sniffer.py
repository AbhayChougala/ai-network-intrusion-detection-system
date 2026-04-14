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

            proto_num = packet.proto
            protocol = protocol_map.get(proto_num, str(proto_num))
            length = len(packet)

            packet_data.append([src_ip, dst_ip, protocol, length])
    except:
        pass

def capture_packets():
    global packet_data
    packet_data = []

    sniff(prn=process_packet, count=50)

    df = pd.DataFrame(packet_data, columns=["Source IP", "Destination IP", "Protocol", "Length"])
    df.to_csv("logs.csv", index=False)

    return df