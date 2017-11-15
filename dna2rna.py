file = open('datasets/rosalind_rna.txt','r')
dna = file.read()
rna = ""
for letter in dna:
    if letter == 'T':
        letter = 'U'
        rna += letter
    else:
        if letter == 'G':
            rna += letter
        else:
            if letter == 'A':
                rna += letter
            else:
                if letter == 'C':
                    rna += letter
print rna
