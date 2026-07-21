# Take input for num1 and num2
num1 = int(input('Enter  number:'))
num2 = int(input('Enter number:'))

# Perform addition
sum = num1 + num2

# Display the result
print(sum)
print('Addition:',sum)
print('Addition is ' + str(sum))
print(f'Addition of {num1} & {num2} is: {sum}')
print('Addition of {} & {} is: {}'.format(num1, num2, sum))
print('Addition of {0} & {1} is: {2}'.format(num1, num2, sum))
print('Addition of {num1} & {num2} is: {sum}'.format(num1=num1, num2=num2, sum=sum))
