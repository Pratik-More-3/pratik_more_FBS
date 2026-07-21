# WAP to print the Fibonacci series up to a given number of terms.
n = int(input("How many fibonacci numbers you want: "))
a =-1
b = 1

for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c

