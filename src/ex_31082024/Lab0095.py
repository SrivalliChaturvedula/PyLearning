class Person:
    # attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # behaviour
    def talk(self):    # self will be the first argument in every behaviour
        print("I can talk")    # No return type, No argument

    def sleep(self, name): # Argument with no return type
        print("Iam a Method")
        print("sleep", name)

    def sleep2(self, name):   # argument with return type
        print("Iam a Method")
        return None

    def walk(self):
        print("Iam walking")

    def walk_return(self):   # No arg with return
        return "Iam walking"

# Create an object of the class
# ObjectRef = ClassName() - > Object

tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk()


rajyalakshmi = Person()
rajyalakshmi.name = "Lakshmi"
print(rajyalakshmi.name)
rajyalakshmi.talk()