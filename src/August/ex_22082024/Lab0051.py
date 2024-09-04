# Match statement: like switch stmt in Java
# match the output and continue

# match variable:
#     case pattern1:
#         # code block 1
#     case pattern2:
#         code block2

# write a program to ask the user which browser he want to use for automation
browser_name = input("Enter name of the browser: ")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute firefox code")
    case "chrome":
        print("Execute the Chrome code")
    case "edge":
        print("Execute edge code")
    case _:
        print("Browser not found")