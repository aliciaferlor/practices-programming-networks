import seq0
print("""-----| Exercise 6 |------""")

filename = seq0.valid_filename()
seq = seq0.seq_read_fasta(filename)
fragment = seq[:20]
reverse = seq0.seq_reverse(fragment)

print("Sequence: ", fragment)
print("Reverse:", reverse)
