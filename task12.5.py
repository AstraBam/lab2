number = int(input())
count = 1
usual_list = []
result_list = []
while count not in usual_list:
    usual_list.append(count)
    result_list.append(10 * count // number)
    count = 10 * count % number
print(*result_list[usual_list.index(count):], sep='')
