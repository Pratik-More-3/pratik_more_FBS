# 8. Divisible by 7 and Multiple of 5

start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)