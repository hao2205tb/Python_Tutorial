l = [0, 1, 3]
l.extend([1, 2])
print(l)
#>> [0, 1, 3, 1]

l.extend("abc")
print(l)
#>> [0, 1, 3, 1, 'abc']

l.append((1, 2))
print(l)
#>> [0, 1, 3, 1, 'abc', (1, 2)]