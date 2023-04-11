import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count_word = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        count_word[word] = count_word.get(word, 0) + 1

print(count_word)