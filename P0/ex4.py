import seq0
print("""-----| Exercise 4 |------""")

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "G", "T"]

for gene in gene_list:
    seq = seq0.seq_read_fasta("./sequences/" + gene)
    print("Gene", gene + ":")
    for base in base_list:
        print(base + ":", str(seq0.seq_count_base(seq, base)))