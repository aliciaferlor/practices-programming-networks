import seq1


def result(i, sequence):
    print("Sequence", str(i), "(Length:", str(sequence.len()), '):', str(sequence))
    print("Bases: ", sequence.count())
    print("Reversed: ", sequence.reverse())


print("-----| Exercise 7 |-----")
list_seq = list(seq1.test_sequences())

for i in range(0, len(list_seq)):
    result(i, list_seq[i])

