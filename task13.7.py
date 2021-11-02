number = int(input("Введите количество солдат: "))
surname = [input() for i in range(number)]
step = int(input())
count = 0
print(surname[0])
del surname[0]
for i in range(number):
    if len(l) > count + step - 1:
        count += step - 1
        print(surname[count])
        del surname[count]
    else:
        count = 0
        if len(surname) > count:
            print(surname[count])
            del surname[count]
