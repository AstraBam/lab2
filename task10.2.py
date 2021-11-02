number = int(input())
text = input()
for i in range(len(text)):
    count = ord(text[i])
    count1 = count + number
    print(chr(count1), end='')
