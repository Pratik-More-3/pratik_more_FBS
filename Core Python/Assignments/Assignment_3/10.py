# 10. Marriage Eligibility

gender = input("Enter Gender (M/F): ")
age = int(input("Enter Age: "))

if gender=="M" and age>=21:
    print("Eligible")
elif gender=="F" and age>=18:
    print("Eligible")
else:
    print("Not Eligible")