from scapy.all import ARP, Ether, srp, get_if_list, conf
import time
import sys
import os
import platform


from modules.write_files import datetime, Files
from modules.find_to_name import FindName

class ArpScan:

    def __init__(self, target: str):

        self.responses = set()
        self.data_desition = dict()

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
                    
                    self.data_desition["ip"] = dst.psrc
                    self.data_desition["mac"] = dst.hwsrc
                    self.data_desition["host"] = find_name.dns_resolve(self.data_desition.get("ip"))

                    if self.data_desition.get("mac") not in self.responses:
                        print(f"-- {self.data_desition.get("ip")} -- {self.data_desition.get("mac")} -- {self.data_desition.get("host")} -- [is ACTIVE 👁️]")
                        
                    for val in self.data_desition.values():
                        self.responses.add(val)

                time.sleep(5)

        except KeyboardInterrupt:

            if desc_file != None:
                new_files = Files()
                new_files.set_data(self.responses)
                new_files.write_file(desc_file)

            print()
            sys.exit()

