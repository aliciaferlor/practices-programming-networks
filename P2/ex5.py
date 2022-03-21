from Client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081

c = Client(IP, PORT)

s = Seq()
s.read_fasta2('../P0/sequences/FRAT1')
i = 0
count = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    print(c.talk(fragment))