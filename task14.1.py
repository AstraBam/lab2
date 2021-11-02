number = int(input())
list_cooking = []
for i in range(0, number):
    cooking = input()
    list_cooking.append(cooking)
for i in range(0, number):
    if 'лук' not in list_cooking[i]:
        if i < number - 1:
            print(list_cooking[i], end=', ')
        else:
            print(list_cooking[i])
