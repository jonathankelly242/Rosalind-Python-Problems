#Jonathan Kelly
#Rosalind Projects
#Project: Complementing a Strand of DNA

#file = open('datasets/rosalind_revc-2.txt','r')
#dna = file.read()
dna = "TAAACGACAGAGCCTCTTGTTGAAGGCTGCTTATTGTTCGTCACCCACCCCGCTTCCTATACCGCCTGGCGGGGTCTACATCCGGACACAGATGACTTTCGTCGTTACATACCGTTGTGCAGAGAGTAGTAGTGAAGCCCGGCAGTTATGCATGCTACGGGTCGCAATTTATGGAAGCGGAGCATCTCTGCGCTTCGGACACTTACTCATACGAACACAGGCATCTCGCCACGATAGCTATAGTTCTTTTACTTTGGTTAGCGCCCAAGATTGGTGACCCGCTGTAAAGGCTGGTGATTAAGGCTTGCGAAGTATAGGGCACAATAATTGTCGAAGGCGTGCGCTGCCGCGTCTTGGGCCCGTCCTCTCAACTCCCTCCGTACCGCCCGCGTCAGGCCATGCCAATTGGCCTCGTCTACTAGTGCGAGTAGGGCGGGCCGTTCGTAGTATGTTAATGCTGAAACCCATGTCCAGTTAGAATGGTATTATGTGACCGGGCAACCCTATGGCCGTCGTTCAGTAATAAGCTCCGCGCGCCCTTTGATCACCTTTTAGGAACAGCGGCTCGGACAACGCGCAAAGGGGCTTTGTTACCTGTAGCGTGTGGTTTCTCCTCCAACTGAGAGACATCTAATCCATCGACCAGGTCGTCTACAGAGCCACGCGTTCAACAAGGCATCTCAGTGACCTCACGGTTGAAGTAACCGATCTGCTTCGGGAGTACACCCAACCAAGATGTGTCCTAGCGGTTCCCGTCTACACCCGAAGCCTGTCTAATTTTATCTTTACGTATCACCGCAC"
r_dna = ""

for symbol in dna:
  if symbol == 'A':
    r_dna = 'T' + r_dna
  else:
    if symbol == 'T':
      r_dna = 'A' + r_dna
    else:
      if symbol == 'C':
        r_dna = 'G' + r_dna
      else:
        r_dna = 'C' + r_dna
print r_dna
