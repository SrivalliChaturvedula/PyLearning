with open('test.txt', 'r') as file2:
    lines = file2.readlines()
    print(lines)
    for line in lines:
        print(line)