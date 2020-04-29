class Node:
    def __init__(self, val, right, left):
        self.__val = val
        self.__right = right
        self.__left = left

    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left
    def setVal(self, var):
        self.__val = var
    def setRight(self, var):
        self.__right = var
    def setLeft(self, var):
        self.__left = var

    def __str__(self):
        return str(self.__val)
