from seq1 import Seq
print('-----| Exercise 4 |------')

seq1 = Seq()
seq2 = Seq("ACGT")
seq3 = Seq("Invalid sequence")

print("Sequence 1: ", "(length:",seq1.len(),')',  seq1)
print("Sequence 2: ", "(length:",seq2.len(),')', seq2)
print("Sequence 3: ", "(length:",seq3.len(),')', seq3)