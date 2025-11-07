class Packet:
    def __init__(self, source_ip, dest_ip, payload, priority):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload
        self.priority = priority 


def fifo_scheduler(packet_list):
    """First-Come, First-Served (FIFO) scheduler"""
    return packet_list


def priority_scheduler(packet_list):
    """Priority scheduler — lower priority value = higher priority"""
    return sorted(packet_list, key=lambda pkt: pkt.priority)


# ---------- TEST ----------
if __name__ == "__main__":
    packets = [
        Packet("10.0.0.1", "10.0.0.2", "Data Packet 1", 2),
        Packet("10.0.0.3", "10.0.0.4", "Data Packet 2", 2),
        Packet("10.0.0.5", "10.0.0.6", "VOIP Packet 1", 0),
        Packet("10.0.0.7", "10.0.0.8", "Video Packet 1", 1),
        Packet("10.0.0.9", "10.0.0.10", "VOIP Packet 2", 0)
    ]

    fifo_order = [p.payload for p in fifo_scheduler(packets)]
    priority_order = [p.payload for p in priority_scheduler(packets)]

    print("FIFO:", fifo_order)
    print("Priority:", priority_order)