from BinaryTree import Tree

class SymbolTable:
    def __init__(self):
        self.__binaryTree = Tree()

    def add(self, value):
        return self.__binaryTree.add(value)
    
    def __str__(self):
        return str(self.__binaryTree)