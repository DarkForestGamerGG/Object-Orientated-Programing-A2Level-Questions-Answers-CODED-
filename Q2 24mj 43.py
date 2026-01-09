
class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):  #constructor
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen

    def GetTreeName(self):
        return self.__TreeName
    def GetHeightGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEvergreen(self):
        return self.__Evergreen


def ReadData():
    TreeObjects = []
    try:
        with open("Trees.txt", "r") as File:
            TreeData = File.read().splitlines()
        for Line in TreeData:
            if not Line.strip():
                continue
            Item = Line.split(",")
            if len(Item) == 5:
                # Create the Tree object
                new_tree = Tree(
                    Item[0],  # Name/Type
                    int(Item[1]),  # Value 1
                    int(Item[2]),  # Value 2
                    int(Item[3]),  # Value 3
                    Item[4]  # Category/Color
                )
                TreeObjects.append(new_tree)

    except IOError:
        print("Error: Could not find or read Trees.txt")

    return TreeObjects