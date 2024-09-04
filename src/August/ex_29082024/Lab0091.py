# Dictionary : key and value pairs, unordered collection
my_dict = {"name": "Srivalli",
           "age": "22",   # latest value will be considered, keys are always unique
           "address": {"HYD", "NDG"}
           }

my_dict_new = {"name": "Srivalli",
           "age": "22",   # latest value will be considered, keys are always unique
           "address": {"HYD", "NDG"}
           }

print(my_dict)
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['address'])

my_dict['age'] = 45
print(my_dict)

my_dict2 = dict(name="Pramod", age=78, address="GA")  # another way of creating dict but don't use this
print(my_dict2)

student_list = [my_dict, my_dict_new]
print(student_list)