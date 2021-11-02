text = input()
count = 0
for i in text:
    if i not in [" ", "\t"]:
        count += 1
print(count)