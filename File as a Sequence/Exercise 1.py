fo = open("mbox-short.txt")

#line = fo.read()
#print(line)

for line in fo:
    line = line.rstrip().upper()
    print(line)

# Close opened file
fo.close()