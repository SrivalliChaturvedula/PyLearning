from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser:

    @abstractmethod
    def startBrowser(self):
        pass
    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stopping")

    def readFromexcel(self):
        print("readFromexcel is ready")


    def runTC(self):
        self.startBrowser()
        self.readFromexcel()
        self.stopBrowser()


Testcase1 = TC1()
Testcase1.runTC()