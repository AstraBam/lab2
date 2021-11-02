number = int(input())
first = [int(input()) for i in range(number)]
second = list(first)
n = int(input())
for i in range(n):
    brother = int(input())
    if brother == 1:
        first[int(input())] += int(input())
    elif brother == 2:
        second[int(input())] += int(input())
print(*first)
print(*second)
coincidence = 0
for i in range(len(first)):
    if first[i] == second[i]:
        coincidence += 1
print(coincidence)
