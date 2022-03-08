from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 6123

c = Client(IP, PORT)
response = c.talk('HEY')

print('Response:', response)