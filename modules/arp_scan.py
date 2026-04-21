from scapy.all import ARP, Ether, srp, get_if_list
import time
import sys
import os
import platform


from modules.write_files import datetime, Files
from modules.find_to_name import FindName

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
        
        print("=" * 67 + "\n")
        self.arp.show()
        print("=" * 67)
        print(f"        IP      |        MAC       |     HOST    |     STATUS")
        print("=" * 67)


    def Scan(self, desc_file=None):
        find_name = FindName()

        try:
            while True:
                ans, unans = srp(self.packet, timeout=2, verbose=0)

                for src, dst in ans:

                    device_ip = dst.psrc
                    device_mac = dst.hwsrc
                    check_mac = f"{device_mac} -- "

                    device_host = find_name.dns_resolve(device_ip)

                    if check_mac not in self.responses:
                        print(f"-- {device_ip} -- {device_mac} -- {device_host} -- [is ACTIVE 👁️]")

                        self.responses.append(f"-- {device_ip} -- ")
                        self.responses.append(f"{device_mac} -- ")
                        self.responses.append(f" {device_host} --\n")
                        
                time.sleep(6)

        except KeyboardInterrupt:

            if desc_file != None:
                new_files = Files()
                new_files.set_data(self.responses)
                new_files.write_file(desc_file)

            print()
            sys.exit()

