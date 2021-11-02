word = input()
list_word = []
list_word.extend(word)
number_letter = int(input())
length = len(list_word)
if (number_letter <= length) and (number_letter - 1 > 0):
    print(list_word[number_letter - 1])
else:
    print('Ошибка')
