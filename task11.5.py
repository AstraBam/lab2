word = input()
length = len(word)
while length > 2:
    result = ''
    for i in range(0, len(word)):
        if i != 0 and i != len(word) - 1:
            result = result + word[i]
    word = result
    length -= 2
    print(result)
