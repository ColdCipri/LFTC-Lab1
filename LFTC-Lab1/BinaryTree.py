class Node:
    def __init__(self, val, counter):
        self.l = None
        self.r = None
        self.v = val
        self.id = counter

class Tree:
    def __init__(self):
        self.root = None
        self.counter = 1

    def add(self, val):
        if(self.root == None):
            self.root = Node(val, self.counter)
        else:
            self.counter += 1
            self._add(val, self.root, self.counter)
        return self.counter

    def _add(self, val, node, counter):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l, self.counter)
            else:
                node.l = Node(val, self.counter)
        else:
            if(node.r != None):
                self._add(val, node.r, self.counter)
            else:
                node.r = Node(val, self.counter)

    def __str__(self):
        if(self.root != None):
           return str(self._printTree(self.root))

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print (str(node.id) + ' -> ' + (node.v) + ' ')
            self._printTree(node.r)