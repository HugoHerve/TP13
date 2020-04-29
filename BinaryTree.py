from Node import *

class BinaryTree:
    def __init__(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        return node == self.getRoot()

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())

    def sumValues(self, node):
        if node is None:
            return 0
        else:
            return self.sumValues(node.getLeft()) + self.sumValues(node.getRight()) + node.getVal()

    def numberLeaves(self, node):
        if node.getLeft() is  None or node.getRight() is None:
            return 1
        else:
            return self.numberLeaves(node.getRight()) +  self.numberLeaves(node.getLeft())

    def numberInternalNoddes(self, node):
        if node.getLeft() is None or node.getRight() is None:
            return 1
        else:
            return self.numberInternalNoddes(node.getRight()) + self.numberInternalNoddes(node.getLeft())

    def height(self, node):
         if node is None:
            return -1
         else :
            branchegauche = self.height(node.getLeft())
            branchedroite = self.height(node.getRight())
            return max(branchedroite, branchegauche) + 1

    def belongs(self, node, val):
        if node is None:
            return False
        if node.getVal() == val:
            return True
        else:
            return self.belongs(node.getRight(), val) or self.belongs(node.getLeft(), val)






N3 = Node(3,None,None)
N4 = Node(4,None, N3)
N6 = Node(6, None, None)
N5 = Node(5, N6, N4)
N18 = Node(18, None, None)
N21 = Node(21, None, None)
N19 = Node(19, N21, N18)
N17 = Node(17, N19, None)
N1 = Node(12, N17, N5)
Racine = BinaryTree(N1)

print(N19)
print(Racine.isRoot(N1))
print(Racine.size(N1))
print(Racine.printValues(N5))
print(Racine.sumValues(N1))
print(Racine.numberLeaves(N1))
print(Racine.numberInternalNoddes(N4))
print(Racine.belongs(N4,3))


