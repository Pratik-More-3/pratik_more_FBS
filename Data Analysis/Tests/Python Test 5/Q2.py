n = int(input("Enter number of coins: "))

coins = list(map(int, input("Enter coin numbers: ").split()))

for num in coins:
    if coins.count(num) % 2 != 0:
        print("Missing coin:", num)
        break