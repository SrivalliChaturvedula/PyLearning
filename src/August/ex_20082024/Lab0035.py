# Write a program to take a user age and let him know if he can go club

# Logic building:
# user input age -> int
# output -> string

# 2. rough logic
# age > 21: can go
# age < 21: can't go

# Logic building

age = int(input("Enter age: "))
if age >= 21:
    print(f"Can goto club -> {age}")
else:
    print(f"Not allowed to goto club -> {age}")