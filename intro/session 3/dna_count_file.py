def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] = d[b] + 1
    return d

with open("dna", "r") as f:
    dna = f.readlines()
    for seq in dna:
        new_seq = seq.replace("\n", "")
        print("Total lenght is: ", len(new_seq))
        for k,v in count_bases(new_seq).items():
            print(k + ":", v)