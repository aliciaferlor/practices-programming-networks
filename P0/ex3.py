import seq0

list_genes = ["U5", "FRAT1", "ADA"]
for l in list_genes:
    print(len(seq0.seq_read_fasta("./sequences/" + l + ".txt")))

gene = input("choose a gene: ")
f = open(folder + geme)
print(f.read())