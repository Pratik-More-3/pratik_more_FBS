no = int(input("Enter the Number:"))
row = int(input("Enter the Row:"))
col = int(input('Enter the column:'))

for i in range(1, row+1):
  for j in range(1, col+1):
    print(j*no,end=' ')
  print()