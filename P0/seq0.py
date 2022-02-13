def seq_ping():
    print("ok")

def valid_filename():
    exit = False
    while not exit:
        filename = input("Choose a file: ")
        folder = "./sequences/"
        filename = folder + filename
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Try with another")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    count_a, count_c, count_g, count_t = 0
    for i in seq:
        if i == "A":
            count_a += 1
        elif i == "C":
            count_c += 1
        elif i == "G":
            count_g += 1
        elif i == "T":
            count_t += 1
    return count_a, count_c, count_g, count_t
