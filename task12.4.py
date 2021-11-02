word = input()
count = 1
for i in range(len(word)-1):
    if i <= len(word):
        if word[i] == word[i + 1]:
            count += 1
        else:
            a = word[i]
            print(count, word[i])
            count = 1
print(count, word[i])
