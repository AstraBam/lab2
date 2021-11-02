a = []
for i in range(int(input())):
    string = input().split(",")
    a.append(string)
for i in range(int(input())):
    coords = [int(i) for i in input().split(',')]
    d = a[coords[0]]
    word = d[coords[1]]
    print(word)
