class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("reading from excel")


class mySQLDBConnection:
    @staticmethod
    def readMySQL():
        print("reading from my SQL")


class TC1:
    def runTC(self):
        mySQLDBConnection.readMySQL()
        ExcelReader.readExcelFile()


tc1 = TC1()
tc1.runTC()

# Common functions will be added as static methods.
