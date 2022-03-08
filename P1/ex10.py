from seq1 import Seq

def result(gene_name, gene):
    print('Gene ' + gene_name + ': Most frequent Base: ' + str(max(gene.count(), key=gene.count().get)))

print('-----| Exercise 10 |------')

gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']
for gene in gene_list:
    seq = Seq()
    seq.read_fasta('./Sequences/' + gene )
    result(gene, seq)