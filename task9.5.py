menu = int(input())
list_menu = []
for i in range(0, menu):
    dish = input()
    list_menu.append(dish)
day = int(input())
list_day_menu = []
for i in range(0, day):
    number_dish = int(input())
    for j in range(0, number_dish):
        day_menu = input()
        list_day_menu.append(day_menu)
for i in range(0, menu):
    if list_menu[i] not in list_day_menu:
        print(list_menu[i])
