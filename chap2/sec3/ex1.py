x, y, z = 10, 4, 8

result = min(x, y, z)

if x % 2 != 0 and x > result:
    result = x

if y % 2 != 0 and y > result:
    result = y

if z % 2 != 0 and z > result:
    result = z

print(result)
