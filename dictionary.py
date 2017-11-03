string = "We tried list and we tried dicts also we tried Zen"
n = 1
for word in string.split(' '):
    words = {}
    words[word] = 1
    if word==word in words:
        print word
        words[word] = n + 1
    for key, value in words.items():
        print key
        print value
    print words
