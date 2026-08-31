L = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

D = {}

for num in L:
    if num in D:
        D[num] = D[num] + 1
    else:
        D[num] = 1

print(D)