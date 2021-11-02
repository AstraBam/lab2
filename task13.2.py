number = int(input())
sort_list = list()
for str_i in range(number):
    sort_list.append(int(input()))
sort_list.sort()
sort_list.reverse()
for str_i in sort_list:
    print(str_i)
