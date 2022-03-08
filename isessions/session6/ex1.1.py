class Seq:
    def __init__(self):
        self.str_bases = str_bases
        if not self.valid_sequence():
            self.str_bases = "ERROR"
            print("ERROR")
        else:
            print("New sequence created!")

    def __str__(self):
        return self.str_bases

    @staticmethod
    def valid_sequence_2(sequence):
        valid = True
        i = 0
        while i < len(self.str_bases) and valid:
            c = self.str_bases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.str_bases) and valid:
            c = self.str_bases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")