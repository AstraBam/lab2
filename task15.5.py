number = int(input())
queue = []
for i in range(number):
    surname = input().split()
    if 'встал' in surname[1]:
        queue.append(surname[0])
    elif surname[0] == 'Привет,':
        queue.insert(queue.index(surname[1][:-1])+1, surname[2])
    elif surname[1] == 'хватит':
        queue.remove(surname[0][:-1])
print(*queue, sep='\n')
