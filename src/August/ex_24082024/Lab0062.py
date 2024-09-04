def print_arguments(*args):
    #  *args = multiple arguments with no limit -> list
    print(args[0])
    for i in args:
        print(i)


print_arguments("A", "B", "C")
print_arguments("B", "C")
print_arguments("C")
print_arguments("P", 10, True, False)

print("amit")
print("pramod", "amith")
print("pramod", "amith", True)
print("pramod", "amith", True, False)