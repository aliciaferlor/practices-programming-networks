from Client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)


gene_list = ["U5", "FRAT1", "ADA"]
for gene in gene_list:
    s = Seq()
    s.read_fasta2(f"../P0/sequences/{gene}")
    c.debug_talk(f"Sending {gene} Gene to the server...")
    c.debug_talk(str(s))
    print(c)
