class XYZ:
    def f1(self):
        try:
            a = int(input("Enter number: "))
        except Exception as e:
            print("Enter only int value")
        else:
            print(a)
        finally:
            print("Anyhow I will be printed")


xy = XYZ()
xy.f1()
