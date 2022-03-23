import socket
from seq1 import Seq
import termcolor

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

list_seq = ['ACGGTATTCGGTA', 'CGTGTCCACGCCAA', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']

PORT = 8085
IP = "127.0.0.1"

ls.bind((IP, PORT))
count_connections = 0
ls.listen()

termcolor.cprint("Seq server has been configured!", 'white')
client_address_list = []

while True:
    termcolor.cprint("Waiting for Clients to connect", 'white')
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print('Connection: ' + str(count_connections) + '. Client ip, port: ' + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        termcolor.cprint("A client has connected to the server", 'magenta')
        msg_raw = cs.recv(2048)
        message = msg_raw.decode().replace("\n", "").strip()
        split_command = message.split(" ")
        command = split_command[0]


        if command != "PING":
            argument = split_command[1]


        if command == "PING":
            response = "OK!\n"
            print(termcolor.colored(response, "green"))
            cs.send(str(response).encode())

        elif command == 'GET':
            try:
                response = list_seq[int(argument)] + "\n"
                print(response)
            except IndexError:
                response = "There is no sequence with that index. " + str(argument)
                print(response)
            cs.send(response.encode())

        elif command == 'INFO':
            s1 = Seq(argument)
            response = "Total length: " + str(Seq.len(s1)) + "\n" + str(Seq.percentages(s1)) + "\n"
            print(response)
            cs.send(response.encode())

        elif command == 'COMP':
            s1 = Seq(argument)
            response = Seq.complement(s1) + "\n"
            print(response)
            cs.send(response.encode())

        elif command == 'REV':
            s1 = Seq(argument)
            response = Seq.reverse(s1) + "\n"
            print(response)
            cs.send(response.encode())

        elif command == 'GENE':
            folder = "../P0/sequences/ADA"
            s1 = Seq()
            s1.read_fasta(folder)
            response = str(s1) + "\n"
            print(response)
            cs.send(response.encode())
        else:
            response = 'This command is not available.'
            cs.send(str(response).encode())
        cs.close()