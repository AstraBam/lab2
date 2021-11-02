number = int(input())
res = []
for i in range(number):
    res.append((input(), int(input())))
m = len(res)
for i in range(m - 1):
    for j in range(m - i - 1):
        if res[j][1] > res[j + 1][1]:
            res[j], res[j + 1] = res[j + 1], res[j]
k = m // 2
final = res[k:]
first = res[:k]
m = len(final)
for i in range(m - 1):
    for j in range(m - i - 1):
        if final[j] > final[j + 1]:
            final[j], final[j + 1] = final[j + 1], final[j]
        if first[j] > first[j + 1]:
            first[j], first[j + 1] = first[j + 1], first[j]
for i in final:
    print(i[0])

for i in first:
    print(i[0])
