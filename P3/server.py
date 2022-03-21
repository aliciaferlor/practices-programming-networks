import socket
PORT = 8989
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("server configurado!")

while True:
    print("waiting for client to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    print("A client has connected to the server")
    message_raw = cs.recv(2048)
    message = message_raw.decode().replace("\n", "").strip()
    split_command = message.split("")
    print("message received", message)

    if len(split_command) == 1:
        command = split_command[0]
    else:
        command = split_command[0]
        argument = split_command[1]

    if command == "PING":
        response = "OK\n"

    else:
        response = "This command is not available in the server\n"
    cs.send(response.encode())
    cs.close()

