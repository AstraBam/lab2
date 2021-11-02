high = int(input())
weight = int(input())
list_symbols = []
for i in range(0, high):
    symbols = input()
    list_symbols.extend(symbols)
for i in range(0, high, 2):
    for j in range(0, weight, 2):
        if i == 0:
            print(list_symbols[j], end='')
        else:
            print(list_symbols[weight * i + j], end='')
    print('\t')
