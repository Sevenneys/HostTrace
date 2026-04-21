import argparse
import time

from modules.arp_scan import *


class ArgFlasg():

    def __init__(self):

        self.__flag_parser = argparse.ArgumentParser(description="HOSTTRACE [v.0.1.1]")
        self.__add_flag_aS = self.__flag_parser.add_argument('-aS', type=str, required=False, help='Арп-сканирование: проверка живых хостов в сети.')
        self.__add_flag_wF = self.__flag_parser.add_argument('-wF', type=str, required=False, help='Запись-файла: записать результаты сканирования в файл.')
        self.args = self.__flag_parser.parse_args()

    def validation_flags(self):

        if self.args.aS == None:

            print("Флаг не указан")
            
        elif self.args.aS != None:
            new_arp = ArpScan(self.args.aS)
            new_arp.InfoArpScan()

            if self.args.wF != None:
                new_arp.Scan(self.args.wF)
            new_arp.Scan()

        else:
            print(f"Флаг указан: {self.args.aS}")

if __name__ == "__main__":

    start_porject = ArgFlasg()
    start_porject.validation_flags()