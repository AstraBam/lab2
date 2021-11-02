n_str = int(input())
str_list = list()
for str_in in range(n_str):
    str_new = input()
    if str_new[:2] != '%%' and str_new[:4] != '####':
        str_list.append(str_new)
    elif str_new[:2] == '%%':
        str_list.append(str_new[2:])
for str_out in str_list:
    print(str_out)