class node:

    def __init__(self,pointernodedata):
        self.NodeData = pointernodedata
        self.LeftNode = None
        self.RightNode = None

    def GetLeft(self):
        return self.LeftNode

    def GetRight(self):
        return self.RightNode

    def GetData(self):
        return self.NodeData

    def SetLeft(self,NodeValue):
        self.LeftNode = NodeValue

    def SetRight(self,NodeValue):
        self.RightNode = NodeValue


class tree:

    def __init__(self,rootnode):
        self.FirstNode = rootnode

    def GetRootNode(self):
        return self.FirstNode

    def Insert(self):





#main
Node1 = node(10)
Node2 = node(20)
Node3 = node(5)
Node4 = node(15)
Node5 = node(7)
