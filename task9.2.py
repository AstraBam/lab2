from collections import Counter

number = int(input())
list_surname = []
for i in range(number):
    for j in range(int(input())):
        surname = input()
        list_surname.append(surname)
list1 = dict(Counter(list_surname))
for who in list1:
    if list1.get(who) == number:
        print(who)
