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
