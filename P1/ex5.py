from seq1 import Seq

def result(i, sequence):
    print("Sequence", i,":", "Length:", sequence.len(), sequence)
    a, c, g, t = sequence.count_bases()
    print('A: ' + str(a) + ', C: ' + str(c) + ', T: ' + str(t) + ', G: ' + str(g))

print('-----| Exercise 5 |------')

seq1 = Seq()
seq2 = Seq("AAACGT")
seq3 = Seq("Invalid sequence")

result(1, seq1)
result(2, seq2)
result(3, seq3)

