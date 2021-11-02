l = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '],
     'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
     'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   ']}
string = input()
for i in range(5):
    for j in string:
        print(l[j][i], end='')
    print('\n')
