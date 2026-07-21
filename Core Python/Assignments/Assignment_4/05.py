# 5. Fibonacci Series

n = int(input("Enter Number of Terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c