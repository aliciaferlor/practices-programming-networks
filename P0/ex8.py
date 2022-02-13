import seq0
print("""-----| Exercise 8 |------""")

gene_list = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
folder = "./sequences/"

for gene in gene_list:
    seq = seq0.seq_read_fasta(folder + gene)
    print("Gene", gene, "most frequent base is: ", str(max(seq0.seq_count(seq), key= seq0.seq_count(seq).get)))