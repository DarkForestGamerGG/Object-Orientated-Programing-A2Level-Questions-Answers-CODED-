class Horse:
    def __init__(self, Name, Maxheight, Percentgage_success):
        self.__Name = Name
        self.__MaxHeight = Maxheight
        self.__PercentageSuccess = Percentgage_success

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxHeight


class Fence:
    def __init__(self, Height, Risk):
        self.__Height = Height
        self.__Risk = Risk

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk

    def __str__(self):
        return f"Fence(Height={self.__Height}, Risk={self.__Risk})"


#main
Horses = [Horse("Beauty", 150, 72), Horse("Jet", 160, 65)]

Course = []
count = 0
Height = 0
Risk = 0
while count < 4:
    found = False
    while found == False:
        Risk = int(input("Enter a valid value: "))
        if Risk >= 1 and Risk <= 5:
            found = True
        else:
            print("Wrong Value Try again!")
    found = False
    while found == False:
        Height = int(input("Enter a valid Value: "))
        if Height >= 70 and Height <= 180:
            found = True
        else:
            print("Wrong Value Try again!")
    Course.append( Fence(Height, Risk))
    count = count + 1
print(Horses[0].GetName())
print(Horses[1].GetName())
print(str(Course[1]))
