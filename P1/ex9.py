from seq1 import Seq


def result(sequence):
    print('Sequence U5' + ': ( Length: ' + str(sequence.len()) + ' ) ' + str(sequence))
    print('Bases: ', sequence.count())
    print('Rev: ', sequence.reverse())
    print('Comp: ', sequence.complement())


print('-----| Exercise 9 |------')
s1 = Seq()
s1.read_fasta('./sequences/U5')
result(s1)