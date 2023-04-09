fname = input('Enter File : ')
if len(fname) < 1:
    fname = 'intro.txt'
fo = open(fname)

di = dict()
for line in fo:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

flip = list()
for k, v in di.items():
    val_key = (v,k)
    flip.append(val_key)

flip = sorted(flip, reverse = True)
for count, word in flip[:5]:
    print(word, count)