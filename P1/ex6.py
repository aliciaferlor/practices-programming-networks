import seq1

def result(i, sequence):
    print("Sequence", i,":", "Length:", sequence.len(), sequence)
    sequence.count_bases()
    print("Bases:", sequence.count())

print('-----| Exercise 6 |------')

list_sequences = list(seq1.test_sequences())
for i in range(0, len(list_sequences)):
    result(i, list_sequences[i])