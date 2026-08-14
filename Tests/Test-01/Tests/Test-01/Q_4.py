area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter cost of interior painting per sq.ft: "))
exterior_cost = float(input("Enter cost of exterior painting per sq.ft: "))

interior_area = area * 2
exterior_area = area * 6

interior_total = interior_area * interior_cost
exterior_total = exterior_area * exterior_cost

total_cost = interior_total + exterior_total

print("Interior painting cost =", interior_total)
print("Exterior painting cost =", exterior_total)
print("Total painting cost =", total_cost)