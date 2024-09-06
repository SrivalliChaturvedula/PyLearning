# Encapsulation - data members in class has to be accessed by only methods available in class

class Myclass:
    # public_variable (instance variable) - accessible by anyone in the program which is created in the class.
    public_var = "Iam Public"
    balance = 0

    # private variable - these can not be accessed outside the class
    __private_var = "Iam private"
    __password = "1234"

    # protected variable - this is available within the Python package, not available outside the package
    _protected_var = "Iam protected"


object = Myclass()
print(object.public_var)
print(object._protected_var)
print(object.balance)
#  print(object.private_var), print(object.password) this can not be done
