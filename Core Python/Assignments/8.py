import random
userID = input("Enter your user ID: ")
password = input("Enter your password: ")

if userID == "admin" and password == "admin123":
  captcha = random.randint(1000, 9999)
  print(f"Your Captcha is: {captcha}")
  chuser=int(input("Enter the Captcha: "))
  if chuser==captcha:
    print("Login Successful!")
  else:
    print("Captcha is incorrect. Login Failed!")
else:
  print("Invalid user ID or password. Login Failed!")