import seq0
print("""-----| Exercise 5 |------""")

gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
folder = "./sequences/"

for gene in gene_list:
    seq = seq0.seq_read_fasta(folder + gene)
    print("Gene", gene + ":", str(seq0.seq_count(seq)))