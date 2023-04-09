fo = open('mbox-short.txt')

for line in fo:
    line = line.rstrip()
    word = line.split()
    if len(word) < 1 or word[0] != 'From':
        continue
    print(word[2])