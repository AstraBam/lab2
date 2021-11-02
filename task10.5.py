list_long_word = []
long_word = input()
list_long_word.extend(long_word)
while list_long_word[0] == 'А' or list_long_word[0] == 'а':
    list_long_word = list()
    long_word = input()
    list_long_word.extend(long_word)
