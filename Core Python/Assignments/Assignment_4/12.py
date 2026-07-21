# 12. Armstrong Number

num = int(input("Enter Number: "))

temp = num
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")