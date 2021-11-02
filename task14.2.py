workers = []
data = input()
while data != "":
    data = list(data.split(","))
    data = list(data[0].split(":"))
    workers.append(data)
    data = input()
password = list(input().split(";"))
for i in range(len(workers)):
    if workers[i][1] in password:
        print(workers[i][0])
        print(str(workers[i][4]) + ", Ваш пароль сликом простой, смените его.")
