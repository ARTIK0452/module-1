def readWords(filename):
    with open(filename) as f:
        for line in f:
            words = ''.join(s for s in line if s.isalpha() or s.isspace())
            for word in words.split():
                yield word.lower()

list = []
dict = {}
i = 0

for word in readWords(input()):
    list.append(word)
newlist = sorted(list)

while i <= len(newlist):
    dict[newlist[i]] = newlist.count(newlist[i])
    i += 1
    if i > len(newlist) -1:
        break

sorteds = sorted(dict.items(), key=lambda x: x[1], reverse=True)

for index, item in enumerate(sorteds):
    print(item[0])
    if index == 4:
        break
