# Program to calculate Compound Interest

P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time (T) in years: "))

A = P * (1 + R / 100) ** T
CI = A - P

print("Compound Interest =", CI)
print("Total Amount =", A)