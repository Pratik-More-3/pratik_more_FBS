L1 = [1, 2, 3, 4]
L2 = [3, 4, 5, 6]

union = []

for num in L1:
    if num not in union:
        union.append(num)

for num in L2:
    if num not in union:
        union.append(num)

print(union)