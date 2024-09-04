# Take user input and create a class
class Person:
    def __init__(self):
        self.name = input("Enter the name: \n")
        self.age = input("Enter age: \n")
        self.phone = input("Enter phone number: \n")
        self.occupation = input("Enter occupation: \n")

    def displayInformation(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone number is {self.phone}")
        print(f"Occupation is {self.occupation}")


# Create an object

person1 = Person()     # init function will be automatically called during object creation

# Call the display function
person1.displayInformation()