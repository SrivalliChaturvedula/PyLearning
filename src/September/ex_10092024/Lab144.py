import os

# operating system module - files, path related to OS

print(os.name)

# for windows laptop - nt

print(os.getcwd())

# os.chdir(r'C:\Users\Chatu\PycharmProjects\PyLearning\src\September\ex_10092024\new_directory')
# print(os.getcwd())

# os.mkdir('new_directory')
# os.makedirs('parent/child/grandchild')

# print(os.listdir('.'))
for file in os.listdir('.'):
    print(file)

# os.remove('example.txt')
# os.rmdir('new_directory')
# os.rmdir('parent/child/grandchild')
# os.rmdir('parent/child')
# os.rmdir('parent')

full_path = os.path.join(r'C:\Users\Chatu\PycharmProjects\PyLearning\src\September\ex_10092024', 'file.txt' )
print(full_path)

print(os.path.exists('file.txt'))
print(os.path.isfile('Lab144.py'))
print(os.path.isdir(r'C:\Users\Chatu\PycharmProjects\PyLearning\src\September\ex_10092024'))
