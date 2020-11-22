
class TreeNode:   # A class representing a node in the Binary Search Tree

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasRightChild(self):
        return self.rightChild

    def hasLeftChild(self):
        return self.leftChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def replaceNodeData(self, key, val, lc, rc):

        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self

        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:              # A class representing a Binary Search Tree

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return  self.size

    def __len__(self):
        return self.size

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)

        else:
            self.root = TreeNode(key, value)
        self.size+=1

    def _put(self, key, value, currentNode):

        if key < currentNode.key:

            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)

            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)

        else:

            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)

            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)


    def get(self, key):

        if self.root:

            res = self._get(key, self.root)

            if res:
                return res.payload

            else:
                return None

        else:
            return None

    def _get(self, key, currentNode):

        if not currentNode:
            return None

        elif currentNode.key == key:
            return currentNode

        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)

        else:
            return self._get(key, currentNode.rightChild)


    def delete(self, key):

        if self.size > 1:

            nodeToBeDeleted = self._get(key, self.root)

            if nodeToBeDeleted:
                self.remove(nodeToBeDeleted)
                self.size-=1

            else:
                raise KeyError("Error: Key not found.")

        elif self.size==1 and self.root.key == key:
            self.root = None
            self.size-=1

        else:
            raise KeyError("Error: Key not found.")


    def findMinChild(self):
        current = self
        if current:
            current = current.leftChild
        return current

    def spliceOut(self):

        if self.isLeaf():

            if self.isLeftChild():
                self.parent.leftChild = None

            else:
                self.parent.rightChild = None


        if self.hasAnyChildren():

            if self.hasRightChild():

                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild

                else:
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent


            else:

                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                    self.leftChild.parent = self.parent


                else:
                    self.parent.rightChild = self.leftChild


    def findSuccessor(self):
        succ=None
        if self.hasRightChild():
            succ = self.rightChild.findMinChild()

        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent


                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccssor()
                    self.parent.rightChild = self

        return succ

    def remove(self, currentNode):

        if currentNode.isLeaf():

            if currentNode.parent.leftChild == currentNode:
                self.parent.leftChild = None

            else:
                self.parent.rightChild = None


        elif self.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:

            if currentNode.hasLeftChild():

                if currentNode.isLefChild():
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent


                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.leftChild.parent = currentNode.parent



                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)


            else:
                if currentNode.isLefChild():
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent


                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.rightChild.parent = currentNode.parent

                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)











