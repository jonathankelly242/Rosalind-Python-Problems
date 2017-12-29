#Jonathan Kelly
#Rosalind Projects
#Project: Counting Point Mutations
lines = open('datasets/rosalind_hamm.txt').read().splitlines()
s = lines[0]
t = lines[1]
count = 0
for i, j in zip(s, t):
    if i != j:
        count = count + 1
print count
