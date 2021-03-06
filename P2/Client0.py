import socket
from termcolor import colored


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        info = 'Connection to server at ' + self.ip + ', PORT : ' + str(self.port)
                #f"Connection to server at {self.ip}, PORT {self.port}
        return info

    def ping(self):
        print("ok")

    def talk(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server: ", message)
        s.send(message.encode())
        response = s.recv(2048).decode("utf-8")
        s.close()
        return 'From server: ' + response

    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server:", colored(msg, "blue"))
        s.send(str.encode(msg))
        response = colored(s.recv(2048).decode("utf-8"), "green")
        s.close()
        return "From server: " + response








