file = open('rosalind_ini5.txt', 'r')
n = 0

for line in file:
    n = n + 1
    if n % 2 == 0:
        print line
