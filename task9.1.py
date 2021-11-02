number_home_book = int(input())
number_summer_book = int(input())
list_home_book = []
list_summer_book = []
for i in range(1, number_home_book + 1):
    home_book = input()
    list_home_book.append(home_book)
for i in range(1, number_summer_book + 1):
    summer_book = input()
    list_summer_book.append(summer_book)
for i in range(0, number_summer_book):
    if list_summer_book[i] in list_home_book:
        print('YES')
    else:
        print('NO')
