from Client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
PORT_2 = 8082
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.read_fasta2('../P0/sequences/FRAT1')
i = 0
count = 0
while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    fragment_text = "Fragment " + str(count) + ": " + fragment
    print(fragment_text)
    if count % 2 == 0:
        print(c_2.talk(fragment_text))
    else:
        print(c.talk(fragment_text))