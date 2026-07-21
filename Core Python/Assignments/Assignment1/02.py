# Write a program to converts days into years, weeks and days. Take the number of days as input from the user.

# Take input from the user
days = int(input("Enter the number of days: "))

years = days // 365
# print(years)
days = days % 365
# print(days)
weeks = days // 7
# print(weeks)
days = days % 7
# print(days)
print(f"Years: {years}, Weeks: {weeks}, Days: {days}")





