symbols = input()
print(*[i for i in input().split() if symbols.upper() in i or symbols in i], sep='\n')
