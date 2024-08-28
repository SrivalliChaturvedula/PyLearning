# Decorators in Python
# Way to modify the behaviour of a function without changing its source code.

def my_decorator(func):
    # it has two parts wrap and call
    def wrapper():
        print("before the function is called")
        print("Add helmet")
        func()
        print("after the function is called")
        print("secured driving")

    return wrapper()


#
@my_decorator
def drive_bike():
    print("Iam driving")

@my_decorator
def drive_scooty():
    print("Iam driving scooty")


