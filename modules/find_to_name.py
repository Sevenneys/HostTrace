import socket

class FindName:

    def dns_resolve(self, target_addr):
        try:
            a_name = socket.gethostbyaddr(target_addr)[0]
        except socket.herror:
            a_name = "Unknow"
        return a_name

    



        