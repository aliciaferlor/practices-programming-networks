import socket


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("ok")

    def __str__(self):
        info = 'Connection to server at ' + self.ip + ', PORT : ' + str(self.port)
                #f"Connection to server at {self.ip}, PORT {self.port}
        return info

    def talk(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server: ", message)
        s.send(str.encode(message))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return 'From server: ' + response










