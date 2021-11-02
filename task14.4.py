integers = list(map(int, input().split()))
xmax = len(integers)
ymax = max(integers)
print("*" * (xmax + 2))
print("*" + " " * xmax + "*")
for y in range(1, ymax + 1):
    print(end="*")
    for k in integers:
        if k >= ymax - y + 1:
            print(end="*")
        else:
            print(end=" ")
    print("*")
