class GF:
    def Car(self):
        return "Nano Car"
class Father(GF):
    def Car(self):
        return "Honda Car"

class Son(Father):
    def Car(self):
        return "Benz car"

son = Son()
print(son.Car())