x = 8
c = 0
odd = 1

while x != 0:
    if x - odd >= 0:
        x -= odd
    else:
        break
    c += 1
    odd += 2
print(c)
