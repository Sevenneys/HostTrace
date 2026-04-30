from scapy.all import ARP, Ether, srp, get_if_list, conf
from rich.console import Console
import time
import sys
import os
import platform

from datetime import datetime
from modules.write_files import datetime, Files
from modules.find_to_name import FindName

class ArpScan:

    def __init__(self, target: str):

        self.console = Console()
        self.new_files = Files()

        self.responses = set()
        self.json_st = {}
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
        print("=" * 105)
        print("=" * 105)


    def Scan(self, desc_file=None):
        find_name = FindName()

        try:
            while True:
                date = str(datetime.now())[:19]
                ans, unans = srp(self.packet, timeout=2, verbose=0)

                for src, dst in ans:
                    
                    ttl = find_name.get_ttl(dst.psrc)
                    if ttl == None:
                        ttl = "Filtered || Loss"

                    self.data_desition["ip"] = dst.psrc
                    self.data_desition["mac"] = dst.hwsrc
                    self.data_desition["host"] = find_name.dns_resolve(self.data_desition.get("ip"))
                    self.data_desition["ttl"] = ttl

                    # self.json_st[date] = self.data_desition

                    if self.data_desition.get("mac") not in self.responses:
                        print(f"-- [IP] {self.data_desition.get("ip")} -- [MAC] {self.data_desition.get("mac")} -- [HOST] {self.data_desition.get("host")} -- [TTL] {self.data_desition.get("ttl")} -- [STATUS] is ACTIVE 👁️ --")
                    
                        
                    if desc_file != None:
                        self.new_files.set_data(self.json_st)
                        self.new_files.write_file(desc_file)


                    for val in self.data_desition.values():
                        self.responses.add(val)

                time.sleep(5)

        except KeyboardInterrupt:
            print()
            sys.exit()

