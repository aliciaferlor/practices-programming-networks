#server

import socket
from seq1 import Seq
def count_bases(seq):
    d =
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    #p = {"a": 0, }
    for k, v in d.items():
        d[k] = [(v*100) / total]
    return d

def convert_message(base_count, base_percentage):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v)+ "(" + str(base_percentage[k]+ "%)" + "\n"
    return message

def info_operation(arg):
    base_count = count_bases(arg)
    response = "Seqiuence: " + arg + "\n"
    response += "lenght: " + str(len(arg)) + "\n"
    response += convert_message(base_count)
    return



split_list =
cmd = split_list[0]

    if cmd != "PING":
        arg = split_list[1]

    if cmd = "PING":
        response = "PING OK"
    elif cmd == "REV":
        response = arg[::-1]
    elif cmd == "INFO":
        response = info_operation(arg)
    elif cmd == "COMP":
        #wrong: response = Seq.complement(arg)
        sequence = Seq(arg)
        response = sequence.complement
    elif cmd== "GET":
        try:
            index = int(arg)
            sequence = SEQUENCES[index]
        except ValueError:
            reponse =
        except IndexError:
            response =


# terminal

echo "PING" | ./nc 127.0.0.1


#client
s.connect
print("* TESTING PING")
s.send(str.encode("ping"))

msg = s.recv(2048)
print(msg.decode("utf-8"))


c = Client(IP, PORT)
print("* Testing Get")  # no inputs
msg = c.talk("GET 0")
print("get 0: ", msg.decode("utf-8"))

s.send(str.encode("Get 0"))

s.close()