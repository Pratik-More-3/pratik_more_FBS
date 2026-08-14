n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1

    if factors == 2:
        print(num, end=" ")
        count += 1

    num += 1