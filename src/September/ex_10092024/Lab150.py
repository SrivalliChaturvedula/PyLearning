# File handling

import os

file = open('test.txt', 'r')
content = file.read()
print(content)

file2 = open(r'C:\Users\Chatu\PycharmProjects\PyLearning\src\September\normal_dir\testing.txt', 'r')
content2 = file2.read()
print(content2)

full_path = os.path.join(r"C:\Users\Chatu\PycharmProjects\PyLearning\src\September\normal_dir", 'test_path.txt')
file3 = open(full_path, 'r')
content3 = file3.read()
print(content3)