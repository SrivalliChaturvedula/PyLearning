a, b, c = (10, 11, 12)
print(a)
print(b)
print(c)

cities = ("London", "Paris", "India")
print("India" in cities)
print("Chennai" in cities)

# cities.append() tuples cannot be appended

t = (12, 34, 56)
my_list = list(t)
my_list.append(36)
print(tuple(my_list))
