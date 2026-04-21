from scapy.all import ARP, Ether, srp, get_if_list
import time
import sys
import os
import platform

class ArpScan:

    def __init__(self, target: str):

        self.target = target
        self.arp = ARP(pdst=self.target)
        self.eth = Ether(dst="ff:ff:ff:ff:ff:ff")
        self.packet = self.eth / self.arp
        self.oc = platform.system().lower()

    def InfoArpScan(self):

        if self.oc == "linux":
            os.system("clear")
        elif self.oc == "windows":
            os.system("cls")

        print()
        
        print("=" * 50 + "\n")
        self.arp.show()
        print("=" * 50)
        print(f"IP | MAC | Vendor | Hostname | Status")
        print("=" * 50)

        
    def Scan(self):

        responses = []

        try:
            while True:
                ans, unans = srp(self.packet, timeout=2, verbose=0)

                for src, dst in ans:

                    device_ip = dst.psrc
                    device_mac = dst.hwsrc

                    if device_mac not in responses:
                        print(f"{device_ip} {device_mac} [is ACTIVE 👁️]")

                    responses.append(device_mac)

                time.sleep(6)

        except KeyboardInterrupt:
            print()
            sys.exit
