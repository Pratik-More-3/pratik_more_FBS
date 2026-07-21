gender = input('Enter your gender (M/F): ')
age = int(input('Enter your age: '))

if (gender == 'M'):
    if (age >= 18):
        print('You are eligible for the men\'s category.')
    else:
        print('You are not eligible for the men\'s category.')
elif (gender == 'F'):
    if (age >= 18):
        print('You are eligible for the women\'s category.')
    else:
        print('You are not eligible for the women\'s category.')