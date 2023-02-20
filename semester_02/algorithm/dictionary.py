word = {}

file = open("ref.txt", "r")
line = file.readline()
while line != "":
    wordlist = line.split()
    for Index in range(len(wordlist)):
        if wordlist[Index] not in word:
            word[wordlist[Index]] = 1
        else:
            word[wordlist[Index]] += 1
    line = file.readline()
file.close()
print(word)
