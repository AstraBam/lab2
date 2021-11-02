number = int(input())
fridge = set()
cook = set()
for i in range(number):
    fridge.add(input())
m = int(input())
for i in range(m):
    recipe = input()
    k = int(input())
    flag = True
    for j in range(k):
        cook.add(input())
    for product in cook:
        if product not in fridge:
            flag = False
    if flag:
        print(recipe)
    cook = set()
