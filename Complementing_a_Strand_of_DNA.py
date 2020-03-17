with open('data/rosalind_revc.txt') as input_data:
    dna = input_data.read().strip("\n")
answer = ""

dna = dna[::-1] #reverse string
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for nuc in dna:
    answer += complement[nuc]

print()
print(answer)