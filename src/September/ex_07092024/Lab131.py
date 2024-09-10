from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def setGear(self):
        pass

class Engine:

    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def setGear(self):
        print("gearbox is ready")


    def drive(self):
        self.start()
        self.setGear()
        self.stop()


car = Car()
car.drive()

