#Ex.3.10 week3
# Sequence alignment

from Bio import SeqIO
handle = open("ls_orchid.fasta")
record_iterator = SeqIO.parse(handle, "fasta")
rec_one = next(record_iterator)
rec_two = next(record_iterator)
handle.close()
seq_one = rec_one.seq
seq_two = rec_two.seq
################################################

#compare sequences

window = 5 # No of characters taken
data = []
#data.append(2+4j)
for i in range(len(seq_one)-window):
    for j in range(len(seq_two)-window):
        if str(seq_one[i:i+window]) == str(seq_two[j:j+window]):
            data.append(i+j*1j)
            #print seq_one[i:i+window],'   ',seq_two[j:j+window]
            
################################################

#plot the results

import dateutil
import matplotlib.pyplot as plt
import pylab
pylab.gray()
x = []
y = []
for num in data:
    x.append(num.real)
    y.append(num.imag)

plt.plot(x,y,'.')
plt.xlabel("%s (length %i bp)" % (rec_one.id, len(rec_one))) 
plt.ylabel("%s (length %i bp)" % (rec_two.id, len(rec_two))) 
plt.title("Dot plot using window size %i\n(allowing no mis-matches)" % window) 
plt.show()


from Bio import Phylo
tree=Phylo.read("tree.txt","newick")
tree.rooted= True
Phylo.draw(tree)
