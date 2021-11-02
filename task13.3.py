number = int(input())
number1 = number
some_list = [0]
while number1 > 0:
    count = 0
    for i in range(1, len(some_list) + 1):
        if some_list[i - 1] == some_list[-i]:
            count += 1
    some_list.append(count)
    number1 -= 1
for i in range(0, number):
    print(some_list[i])
