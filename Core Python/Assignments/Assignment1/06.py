# Program to find the third angle of a triangle

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))

angle3 = 180 - (angle1 + angle2)

print("The third angle is =", angle3)