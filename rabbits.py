#Jonathan Kelly
#Rosalind Projects
#Project: Rabbits and Recurrence Relations

def rabbitPairs(numMonths, numOffspring):
    if (numMonths == 1):
        return 1;

    else:
        if (numMonths == 2):
            return numOffspring;

    oneGenBack = rabbitPairs(numMonths-1, numOffspring);
    twoGenBack = rabbitPairs(numMonths-2, numOffspring);

    if (numMonths <= 4):
        return (oneGenBack + twoGenBack);
    return (oneGenBack + (twoGenBack * numOffspring));

answer = rabbitPairs(33,3);
print answer
