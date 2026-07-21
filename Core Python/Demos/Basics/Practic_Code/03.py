# WAP to calculate Simple Interest

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))

simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest

print("\nSimple Interest =", simple_interest)
print("Total Amount =", amount)