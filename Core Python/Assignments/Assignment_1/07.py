# Program to find the roots of a quadratic equation

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = (b * b) - (4 * a * c)

if d > 0:
    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2 * a)
    print("Both roots are equal.")
    print("Root =", root)

else:
    print("Roots are imaginary (cannot be calculated without complex numbers).")