with open('data/rosalind_rna.txt') as input_data:
    dna = input_data.read()

rna = dna.replace("T", "U")
print(rna)