number_buy = int(input())
shop_list = []
for i in range(0, number_buy):
    buy = input()
    piece_number = input()
    shop_list.append(buy + ' ' + piece_number)
    print(shop_list)
for i in range(1, number_buy + 1):
    print(shop_list[-i])
