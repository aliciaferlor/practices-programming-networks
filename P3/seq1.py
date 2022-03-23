class Seq:
    """A class for representing sequences"""

    null_seq = "NULL"
    invalid_seq = "ERROR"

    def __init__(self, str_bases=null_seq):
        if str_bases == Seq.null_seq:
            self.str_bases = str_bases
            print("NULL seq created")
        elif Seq.valid_sequence_2(str_bases):
            self.str_bases = str_bases
            print("New sequence created!")
        else:
            self.str_bases = Seq.invalid_seq
            print("INCORRECT Sequence detected.")

    @staticmethod
    def valid_sequence_2(str_bases):
        for i in str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    def valid_sequence(self):
        for i in self.str_bases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.str_bases

    def len(self):
        """Calculate the length of the sequence"""
        if self.valid_sequence():
            return len(self.str_bases)
        else:
            return 0

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.str_bases == Seq.null_seq or self.str_bases == Seq.invalid_seq:
            return a,c,g,t
        else:
            for e in self.str_bases:
                if e == "A":
                    a += 1
                elif e == "T":
                    t += 1
                elif e == "G":
                    g += 1
                elif e == "C":
                    c += 1
        return a, c, g, t

    def count(self):
        a, c, t, g = self.count_bases()
        return {'A': a, 'C': c, 'T': t, 'G': g}

    def percentages(self):
        a, c, t, g = self.count_bases()
        per_a = "(" + str(round(a / self.len() * 100, 1)) + "%)"
        per_c = "(" + str(round(c / self.len() * 100, 1)) + "%)"
        per_t = "(" + str(round(t / self.len() * 100, 1)) + "%)"
        per_g = "(" + str(round(g / self.len() * 100, 1)) + "%)"
        return "A: " + str(a) + "  " + per_a + "\n" + "C: " + str(c) + "  " + per_c + "\n" + "T: " + str(
            t) + "  " + per_t + "\n" + "G: " + str(g) + "  " + per_g

    def reverse(self):
        if self.str_bases == Seq.null_seq:
            return 'NULL'
        elif self.str_bases == Seq.invalid_seq:
            return 'ERROR'
        else:
            return self.str_bases[::-1]

    def complement(self):
        if self.str_bases == Seq.null_seq:
            return 'NULL'
        elif self.str_bases == Seq.invalid_seq:
            return 'ERROR'
        else:
            complement = ""
            for ch in self.str_bases:
                if ch == "A":
                    complement += "T"
                elif ch == "T":
                    complement += "A"
                elif ch == "G":
                    complement += "C"
                elif ch == "C":
                    complement += "G"
            return complement

    @staticmethod
    def frequent_base(dict_count):
        return max(dict_count, key=dict_count.get)

    @staticmethod
    def line(seq):
        return seq[seq.find('\n'):].replace('\n', '')

    def read_fasta(self, filename):
        from pathlib import Path
        self.str_bases = Seq.line(Path(filename).read_text())

def test_sequences():
    seq1 = Seq()
    seq2 = Seq("AAACGT")
    seq3 = Seq("Invalid sequence")
    return seq1, seq2, seq3



