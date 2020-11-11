#This is implementation of a Binary Tree using references

class BinaryTree:

   def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

   def insertLeft(self, newNode):
        if self.leftChild==None:
            self.leftChild = BinaryTree(newNode)

        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp


    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            temp = BinaryTree(newNode)
            temp.rightChild=self.rightChild
            self.rightChild=temp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key




