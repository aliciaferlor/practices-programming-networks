import seq0
print("""-----| Exercise 7 |------""")

filename = seq0.valid_filename()
seq = seq0.seq_read_fasta(filename)
fragment = seq[:20]
complement = seq0.seq_complement(fragment)

print("Fragment of DNA sequence:", fragment)
print("Complementary bases sequence:", complement)