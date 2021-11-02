list_long_word = []
long_word = input()
list_long_word.extend(long_word)
if list_long_word[0] == 'А' or 'а':
    print('ДА!')
else:
    print('НЕТ')
