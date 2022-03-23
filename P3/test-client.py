from Client0 import Client

list_seq = ['ACCGTGGTGTAACGAAA', 'ATTTGCTGTCTCT', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']
list_genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)
print('Connection to SERVER. Client ip, port: ', str(IP) + ',', str(PORT))

print("- Testing PING...")
response = c.talk("PING ")
print(f"{response}")

print("- Testing GET...")
for n in range(0, len(list_seq)):
    response = c.talk("GET " + str(n))
    print(f"{response}")

print("- Testing INFO...")
response = c.talk("INFO " + list_seq[0])
print(f"{response}")

print("- Testing COMP...")
response = c.talk("COMP " + list_seq[0])
print(f"{response}")

print("- Testing REV...")
response = c.talk("REV " + list_seq[0])
print(f"{response}")

print("- Testing GENE...")
for gene in list_genes:
    response = c.talk("GENE " + gene)
    print(f"{response}")
