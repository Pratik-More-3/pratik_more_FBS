# WAP to find Quotient and Remainder

# Take input from the user
dividend = int(input("Enter Dividend: "))
divisor = int(input("Enter Divisor: "))

# Calculate Quotient and Remainder
quotient = dividend // divisor
remainder = dividend % divisor

# Display the results
print("Quotient =", quotient)
print("Remainder =", remainder)