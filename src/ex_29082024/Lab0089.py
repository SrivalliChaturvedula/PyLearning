t = ("Testing academy", "789", "789")
print(t)

print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)

set6 = set2.difference(set1)
print(set6)

