import seq0
print("""-----| Exercise 3 |------""")

gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
folder = "./sequences/"

for gene in gene_list:
    print("Gene", gene, "length:", len(seq0.seq_read_fasta(folder + gene )))
