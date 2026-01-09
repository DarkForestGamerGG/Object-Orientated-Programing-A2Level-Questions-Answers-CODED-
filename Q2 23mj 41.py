class Vehicle:

    def __init__(self):
        self.__ID = str
        self.__MaxSpeeed = int
        self.__IncreaseAmount = int
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeeed

    def SetCurrentSpeed(self,speed):
        self.__CurrentSpeed = speed

    def SetHorizontalPosition(self,postion):
        self.__HorizontalPosition = postion

    def IncreaseSpeed(self):
       if (self.__IncreaseAmount + self.__CurrentSpeed) <= self.__MaxSpeeed:
           self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
           self.__HorizontalPosition = self.__CurrentSpeed + self.__HorizontalPosition
       else:
           self.__CurrentSpeed = self.__MaxSpeeed


