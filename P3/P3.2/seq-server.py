import socket
import server_functions
import termcolor

list_seq = ['ACGGTATTCGGTA', 'CGTGTCCACGCCAA', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
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

    termcolor.cprint("A client has connected to the server", 'magenta')
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode().replace("\n", "").strip()
    split_command = msg.split("")

    if len(split_command) == 1:
        command = split_command[0]
    else:
        command = split_command[0]
        argument = split_command[1]

    if command == "PING":
        server_functions.ping(cs)
    elif command == 'GET':
        server_functions.get(cs, list_seq, argument)
    elif command == 'INFO':
        server_functions.info(cs, argument)
    elif command == 'COMP':
        server_functions.comp(cs, argument)
    elif command == 'REV':
        server_functions.rev(cs, argument)
    elif command == 'GENE':
        server_functions.gene(cs, argument)
    else:
        response = 'This command is not available.'
        cs.send(str(response).encode())
    cs.close()


