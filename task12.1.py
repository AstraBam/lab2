number_white = int(input())
list_white = []
for i in range(0, number_white):
    white_word = input()
    list_white.append(white_word)
number_black = int(input())
list_black = []
for i in range(0, number_black):
    black_word = input()
    list_black.append(black_word)
for i in range(0, number_black):
    if list_black[i] in list_white:
        print(list_black[i])
