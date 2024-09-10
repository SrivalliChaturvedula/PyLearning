# Using try except to open a file

try:
    with open('test.txt', 'r') as file:
        content = file.readlines()
        print(content)
except FileNotFoundError as ffe:
    print(ffe)
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)


