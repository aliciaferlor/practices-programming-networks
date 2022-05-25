from seq1 import Seq

def print_colored(message, color):
    from termcolor import colored
    print(colored(message,color))

def ping(cs):
    print_colored("PING", "green")
    response = "OK!\n"
    cs.send(str(response).encode())

def get(cs, list_seq, argument):
    print_colored("GET", "yellow")
    try:
        response = list_seq[int(argument)] + "\n"
        print(response)
    except IndexError:
        response = "There is no sequence with that index. " + str(argument)
        print(response)
    cs.send(response.encode())


def info(cs, seq):
    print_colored("INFO", "magenta")
    s1 = Seq(seq)
    response = "Total length: " + str(Seq.len(s1)) + "\n" + str(Seq.percentages(s)) + "\n"
    print(response)
    cs.send(response.encode())

def comp(cs, seq):
    print_colored("COMP", "cyan")
    s1 = Seq(seq)
    response = Seq.complement(s1) + "\n"
    print(response)
    cs.send(response.encode())

def rev(cs, seq):
    print_colored("REV", "red")
    s1 = Seq(seq)
    response = Seq.reverse(s1) + "\n"
    print(response)
    cs.send(response.encode())

def gene(cs, gene_name):
    print_colored("GENE", "blue")
    folder = "../P0/sequences/" + gene_name
    s1 = Seq()
    s1.read_fasta(folder)
    response = str(s1) + "\n"
    print(response)
    cs.send(response.encode())