# Create a Employee Class
# A - name,age
# B - print details
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print("name:", self.name,
              "age:", self.age)


def get_employee_details():
    name = input("Enter name:")
    age = int(input("Enter age:"))
    return name, age


E1_details = get_employee_details()
E1 = Employee(*E1_details)
E1.print_details()

E2 = Employee(name="Srivalli", age=32)
E2.print_details()
