a = 0
b = 0
c = 8
print("3L  5L  8L")
print(a, b, c)
x = min(c, 5 - b)
c -= x
b += x
print(a, b, c)
x = min(b, 3 - a)
b -= x
a += x
print(a, b, c)
x = min(a, 8 - c)
a -= x
c += x
print(a, b, c)
x = min(b, 3 - a)
b -= x
a += x
print(a, b, c)
x = min(c, 5 - b)
c -= x
b += x
print(a, b, c)
x = min(b, 3 - a)
b -= x
a += x
print(a, b, c)
x = min(a, 8 - c)
a -= x
c += x
print(a, b, c)
print("Target reached!")
