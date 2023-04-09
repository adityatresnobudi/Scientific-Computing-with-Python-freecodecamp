fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
fo = open(fname)

di = dict()
for line in fo:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word,0) + 1

print(max(di), di[max(di)])