a = [100, 96, 87, 100, 1523, 13525]

print(a[0])
print(a[1])

print(a)
print(a[0:5])
print(a[4:5])
print(a[ :4])
print(a[3: ])

b = [[100, 124, 12, 315, 123], [123, 561, 512, 31, 412], [23, 515, 5235, 4124, 123]]
c = [[[100, 12, 152, 35, 1263], 183, 5561, 5142, 731, 12], [3, 51, 52345, 124, 23]]

print(b[0][1])
print(b[1])
print(b[0][2:])
print(b[1:])
print("==============================")

d = [13, 12, 55, 51, 71]
e = d

d[1] = 10

print(d)
print(e)

f = a + d
print(f)

g = a + b
print(g)

h = d * 3
print(h)

print(len(a))
print(len(b))
print(len(b[0]))