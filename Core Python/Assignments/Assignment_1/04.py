# Program to calculate Simple Interest

P = float(input("Enter Principal (P): "))
T = float(input("Enter Time (T) in years: "))
R = float(input("Enter Rate of Interest (R): "))

SI = (P * T * R) / 100

print("Simple Interest =", SI)