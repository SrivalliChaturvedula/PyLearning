from abc import ABC, abstractmethod


class PyATB(ABC):
    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Amith(PyATB):
    def payFee(self):
        print("PAid")


a = Amith()
a.payFee()
