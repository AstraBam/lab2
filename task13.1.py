number = int(input())
l = [''] * number
for i in range(number):
    l[i] = input()
number1 = int(input())
for i in range(number1):
    x = int(input())
    tmp = [''] * x
    for j in range(x):
        tmp[j] = l[int(input()) - 1]
    l = tmp
for i in l:
    print(i)
