# try, except, finally
# file
import os
try:
    full_path = os.getcwd()
    full_path_file = full_path + "/example.txt"
    print(full_path_file)
    
    file = open('example.txt', 'r')
    print(file.read())
except FileNotFoundError as ffe:
    print(ffe)
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)


