# a =10
# if a == 10:
# pass

for i in range(1, 10):
  #pass 
  if  i==7:
    #break
    continue
  print(i)
else:
  print("I am in else block")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(f"Prime numbers between {start} and {end} are:")
for num in range(start,end):
  if num > 1:
      for i in range(2, num):
            if num % i == 0:
                break
      else:
        print(num)
  else:
        print('The number is not prime nor composite')