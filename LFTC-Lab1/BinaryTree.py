class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None
        self.count = 1

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)#TO-DO ADD COUNTER FOR IDENTIFIER

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def __str__(self):
        if(self.root != None):
           return str(self._printTree(self.root))

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print (str(self.count) + ' -> ' + (node.v) + ' ')
            self.count += 1
            self._printTree(node.r)