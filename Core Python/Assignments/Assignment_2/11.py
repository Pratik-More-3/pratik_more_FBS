# 11. Minimum Number of Notes

amount = int(input("Enter amount: "))

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

note5 = amount // 5
amount = amount % 5

note2 = amount // 2
amount = amount % 2

note1 = amount

print("500 =", note500)
print("200 =", note200)
print("100 =", note100)
print("50 =", note50)
print("20 =", note20)
print("10 =", note10)
print("5 =", note5)
print("2 =", note2)
print("1 =", note1)