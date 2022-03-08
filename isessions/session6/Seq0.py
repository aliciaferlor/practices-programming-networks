import termcolor

def seq_ping():
    print("ok")

def valid_filename():
    exit = False
    while not exit:
        name = input("Choose a file: ")
        folder = "./sequences/"
        filename = folder + name
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
    count_a, count_c, count_g, count_t = 0, 0, 0, 0
    for i in seq:
        if i == "A":
            count_a += 1
        elif i == "C":
            count_c += 1
        elif i == "G":
            count_g += 1
        elif i == "T":
            count_t += 1
    base_dic = {"A": count_a, "C": count_c, "G": count_g, "T": count_t}
    return base_dic

def seq_reverse(fragment):
    reverse = fragment[::-1]
    return reverse

def seq_complement(fragment):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    new = ''
    for base in fragment:
        new += complement[base]
    return new

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
        #if Seq.is_valid_sequence_2(strbases):
            print("New sequence created!")
        else:
            self.strbases = 'Error'
            print('Incorrect sequence!')

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence ' + str(i) + ' : (Length: ' + str(list_sequences[i].len()) + ' ) ' + str(list_sequences[i])
            termcolor.cprint(text, 'blue')

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq