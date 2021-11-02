egle_or_tails = input()
list_egle_or_tails = []
list_egle_or_tails.extend(egle_or_tails)
max_egle = 0
count = 0
for i in range(0, len(list_egle_or_tails)):
    if list_egle_or_tails[i] == 'о':
        count += 1
    if count > max_egle:
        max_egle = count
    if i + 1 < len(list_egle_or_tails):
        if list_egle_or_tails[i + 1] == 'р':
            count = 0
print(max_egle)

