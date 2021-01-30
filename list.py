a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[0:3])
print(a[1:])
print(a[:])
print(a[3:3])
print(a[0:8:2])
print(a[::-1])
a.append(10)
print(a)
a.insert(0, 0)
print(a)

b = [11, 12, 13]

a.extend(b)
print(a)

print(a.index(10))

a.sort()
print(a)
a.reverse()
print(a)

a.pop()
print(a)

a.pop(5)
print(a)

a.remove(4)
print(a)

print(a.count(8))

c = a.copy()
print(c)

print(len(a))
print(min(a))
print(max(a))
del(a)
# print(a)

a = [10, 20, 30, 40, 50]

for i in a:
    print(i)

for i in range(0, len(a), 1):
    print(i)

for i in range(0, len(a), 1):
    print(a[i])

q = [1, 2, 3, 4, 5, 6]
q[0] = [100]
print(q)

q = [1, 2, 3, 4, 5, 6]
q[0:3] = [100, 100, 100]
print(q)

q = [1, 2, 3, 4, 5, 6]
q[0:3] = [0]
print(q)

q = [1, 2, 3, 4, 5, 6]
q[0:0] = [100]
print(q)
# cloning using slicing
b = a[:]
print(b)
print(a is b)
# cloning using list()
a = [1, 2, 3, 4, 5]
b = list(a)
print(b)
print(a is b)
a[0] = 100
print(a)
print(b)
# cloning using copy
a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)
print(a is b)
