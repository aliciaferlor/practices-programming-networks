import seq0
filename = seq0.valid_filename()
seq = seq0.seq_read_fasta(filename)
text = seq[:20]

print("DNA file:", "U5")
print("The first 20 bases are:", text)
