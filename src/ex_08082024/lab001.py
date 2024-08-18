# This is a comment - which doesn't run


print("Hello, welcome to Python learning")
print(2+2)

with open("output.txt", "w") as file:
    print("Hello", "World", sep="-", end="!", file=file, flush=True)

