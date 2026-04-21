from scapy.all import ARP, Ether, srp, get_if_list
import time
import sys
import os
import platform


from modules.write_files import datetime, Files

class ArpScan:

    def __init__(self, target: str):

        self.responses = []

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


    def Scan(self, desc_file=None):

        is_call = 1

        try:
            while True:
                ans, unans = srp(self.packet, timeout=2, verbose=0)

                for src, dst in ans:

                    device_ip = dst.psrc
                    device_mac = dst.hwsrc
                    check_mac = f"{device_mac}\n"

                    if check_mac not in self.responses:
                        print(f"{device_ip} {device_mac} [is ACTIVE 👁️]")

                        self.responses.append(f"{device_ip} ")
                        self.responses.append(f"{device_mac}\n")
                        
                time.sleep(6)

        except KeyboardInterrupt:

            if desc_file != None:
                new_files = Files()
                new_files.set_data(self.responses)
                new_files.write_file(desc_file)

            print()
            sys.exit()

