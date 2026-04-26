from scapy.all import IP, ICMP, sr1
import socket

class FindName:


    def dns_resolve(self, target_addr: str):
        try:
            a_name = socket.gethostbyaddr(target_addr)[0]
        except socket.herror:
            a_name = "Unknow"
        return a_name
    

    # Позже
    def get_ttl(self, target_addr: str):
        self.icmp_packet = IP(dst=target_addr) / ICMP()

        icmp_reply =sr1(self.icmp_packet, timeout=1, verbose=0)

        if icmp_reply:
            return icmp_reply.ttl
        else:
            return None



    



        