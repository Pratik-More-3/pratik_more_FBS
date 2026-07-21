# 12. Palindrome Number

num = int(input("Enter Three Digit Number: "))

a = num//100
b = (num//10)%10
c = num%10

reverse = c*100+b*10+a

if num==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
    