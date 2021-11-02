number_men = int(input())
list_surname = []
list_same_surname = []
count = 0
count1 = 0
for i in range(0, number_men):
    surname = input()
    list_surname.append(surname)
for i in range(0, number_men):
    count1 = 0
    if list_surname[i] not in list_same_surname:
        list_same_surname.append(list_surname[i])
        for j in range(i, number_men):
            if list_surname[i] == list_surname[j]:
                count += 1
                count1 += 1
    if count1 == 1:
        count -= 1
print(count)
