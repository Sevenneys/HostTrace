from datetime import datetime

class Files:

    def __init__(self):
        self.__data = [str(datetime.now())[:19] + "\n\n"]


    def set_data(self, data):
        for el in data:
            self.__data.append(el)


    def write_file(self, descriptor: str):

        try:
            with open(descriptor, "a+", encoding="utf-8") as file:
                for str_d in self.__data: 
                    file.write(str_d)
                else:
                    file.write("\n\n")
        except FileNotFoundError:
            print(f"--- Указан не корректный путь --- ❌")


ip_dev = "192.168" + " "
mac_dev = f"2f:34:12" + "\n"
desc = "/home/seven/arp_res.txt"

a = [ip_dev, mac_dev, ip_dev, mac_dev, ip_dev, mac_dev]

new_files = Files()
new_files.set_data(a)
new_files.write_file(desc)





    