#
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, print details,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee:
    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def walk(self):
        print(self.name, "can walk")

    def talk(self):
        print(self.name, "can talk")

    def print_details(self):
        print("name:", self.name,
              "age:", self.age,
              "phone:", self.phone,
              "address:", self.address,
              "eid:", self.eid)


print("Enter Employee 1 details ")
E1 = Employee(name=input("Enter name: "),
              age=int(input("Enter age: ")),
              phone=int(input("Enter phone: ")),
              address=input("Enter Address: "),
              eid=int(input("Enter eid: "))
              )
E1.walk()
E1.talk()
E1.print_details()

print("Enter Employee 2 details ")
E2 = Employee(name=input("Enter name: "),
              age=int(input("Enter age: ")),
              phone=int(input("Enter phone: ")),
              address=input("Enter Address: "),
              eid=int(input("Enter eid: "))
              )
E2.walk()
E2.talk()
E2.print_details()
