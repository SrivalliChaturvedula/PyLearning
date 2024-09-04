squares = [1, 4, 9, 16, 25]

# list is mutable in nature

squares[3] = 64
print(squares)

# tuples are collection of data which are immutable

my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3] = 64 -> assignemnt of values are not allowed in tuples
print(my_tuple)

shopping_list_wife = ['bread', 'butter', 'paneer']
shopping_list_wife[2] = 'milk'
print(shopping_list_wife)

# real world project
# the testing academy.com, sdet.live
my_tuple = ("taa.com", "sdet.live")
my_api_list = list(my_tuple)  # conversion is possible
print(my_api_list)
my_api_list = tuple(my_api_list)
print(my_api_list)
