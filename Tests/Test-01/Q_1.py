length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

pi = 3.14

area = (length * breadth) + (pi * radius * radius / 2)

perimeter = (2 * length) + breadth + (pi * radius)

print("Area =", area)
print("Perimeter =", perimeter)