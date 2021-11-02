key_str = input()
n_pos = int(key_str[:4])
check_sum = int(key_str[4:])
err_list = ''
r_sum = 0
for str_i in range(n_pos):
    r_str = input()
    str1 = int(r_str[:7])
    str2 = int(r_str[8:12])
    str3 = int(r_str[13:])
    if str1 * str2 != str3:
        err_list += str(str_i + 1) + ' '
    r_sum += str1 * str2
print(check_sum - r_sum)
if len(err_list):
    print(err_list)
