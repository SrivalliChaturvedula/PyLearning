public_toilet = "PB"


# local variables have more preference than global variable

def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)


home()


def stranger():
    print(public_toilet)
    # print(private_toilet)


print(public_toilet)
# print(private_toilet)
