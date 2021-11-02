word = input()
word = word.upper()
maximum = 0
for i in range(0, len(word)):
    if word.count(word[i]) > maximum:
        maximum = word.count(word[i])
print(maximum)
