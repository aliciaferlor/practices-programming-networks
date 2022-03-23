import socket
from seq1 import Seq
from termcolor import colored


def print_colored(message, color):
    print(colored(message,color))


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

list_seq = ['ACGGTATTCGGTA', 'CGTGTCCACGCCAA', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']
list_genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

PORT = 8081
IP = "127.0.0.1"

ls.bind((IP, PORT))
count_connections = 0
ls.listen()

print_colored("Seq server has been configured!", 'white')
client_address_list = []

while True:
    print_colored("Waiting for Clients to connect", 'white')
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
        print_colored("A client has connected to the server", 'magenta')
        msg_raw = cs.recv(2048)
        message = msg_raw.decode().replace("\n", "").strip()
        split_command = message.split(" ")
        command = split_command[0]

        if command != "PING":
            argument = split_command[1]
        print_colored(f"Message received: {message}", "cyan")
        if command == "PING":
            print_colored("PING", "green")
            response = "OK!\n"
            cs.send(str(response).encode())

        elif command == 'GET':
            print_colored("GET", "yellow")
            try:
                response = list_seq[int(argument)] + "\n"
                print(response)
            except IndexError:
                response = "There is no sequence with that index. " + str(argument)
                print(response)
            cs.send(response.encode())

        elif command == 'INFO':
            print_colored("INFO", "magenta")
            s1 = Seq(argument)
            response = "Total length: " + str(Seq.len(s1)) + "\n" + str(Seq.percentages(s1)) + "\n"
            print(response)
            cs.send(response.encode())

        elif command == 'COMP':
            print_colored("COMP", "cyan")
            s1 = Seq(argument)
            response = Seq.complement(s1) + "\n"
            print(response)
            cs.send(response.encode())

        elif command == 'REV':
            print_colored("REV", "red")
            s1 = Seq(argument)
            response = Seq.reverse(s1) + "\n"
            print(response)
            cs.send(response.encode())

        elif command == 'GENE':
            print_colored(f"GENE {argument}", "blue")
            folder = "./sequences/"
            s1 = Seq()
            s1.read_fasta(folder + argument)
            response = str(s1) + "\n"
            print(response)
            cs.send(response.encode())
        else:
            response = 'This command is not available.'
            cs.send(str(response).encode())
        cs.close()