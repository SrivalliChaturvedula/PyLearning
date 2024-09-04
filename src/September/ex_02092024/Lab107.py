class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Staring car with name", self.name)
        print("Starting car with make", self.make)
        print("Starting car with model", self.model)

lambo = Car("lambo", "V2", "2024")
lambo.start_engine()