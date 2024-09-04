# List - collection of items (duplicate is allowed)
my_list = [1, 2, 3]
my_list2 = [1, "Pramod", True, 3.14]

print(my_list)
print(len(my_list))
# index always starts with 0
print(my_list[0])
print(my_list[2])
# print(my_list[10]) : index out of range exception

# Indexing
my_list[0] = "Pramod"
my_list[1] = "Dutta"
# my_list[10] = "Sri" : Assignment index out of range exception
print("Element at index0 ->", my_list[0])
print("Element at index1 ->", my_list[1])
print(my_list)

for element in my_list:
    print(element)

# range(1, 10, 1) range itself provides list of numbers specified [1 t0 9]

for i in range(1, 10):
    print(i)

print("-------------------------------")

my_list = [1,2,3]

# Append
my_list.append(4)
# append object at the end of the list, append can add only one object at a time
my_list.append(5)
my_list.append(6)

# extend
my_list.extend([10, 20, 30, 40])  # extend can be used to add number of elements at a time to the list
my_list.extend([50])
my_list.extend([True])
print(my_list)
print(len(my_list))

# insert  # this will insert new value at the specified index
my_list.insert(1,"Dutta")
print(my_list)
print(len(my_list))
my_list.insert(-1, "Sri")
print(my_list)

# no replace in Python, we have to reassign value to change a list value

# remove an element
my_list.remove("Sri")
print(my_list)

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)


print("-------------")

my_copy_list.remove("Dutta")


print("list is: ", my_copy_list)
try:
    my_copy_list.remove(True)
except ValueError:
    pass

print(my_copy_list)
