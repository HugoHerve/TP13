from Node import *

class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

N3 = Node(3,None,None)
N4 = Node(4,None, N3)
N6 = Node(6, None, None)
N5 = Node(5, N6, N4)
N18 = Node(18, None, None)
N21 = Node(21, None, None)
N19 = Node(19, N21, N18)
N17 = Node(17, N19, None)
Racine = BinaryTree(Node(12, N17, N5))






