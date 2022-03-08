from Client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 6123

c = Client(IP, PORT)
response = c.talk('HEY')

print('Response:', response)

s1 = Seq()
filename = s1.get_file()
s1.read_fasta2(filename)

print("")