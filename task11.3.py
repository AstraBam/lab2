word = input()
number = int(input())
letter = input()
list_word = []
list_word.extend(word)
if list_word[number - 1] == letter:
    print('Да!')
elif len(letter) > 1:
    print('ОШИБКА')
else:
    print('НЕТ')
