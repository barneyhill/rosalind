with open('data/rosalind_dna.txt') as input_data:
	dna = input_data.read()

char_count = []
for character in ['A', 'C', 'G', 'T']:
	char_count.append(str(dna.count(character)))

print(" ".join(char_count))