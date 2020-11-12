

class BinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):

        while i//2>0:
            if self.heapList[i//2]>self.heapList[i]:
                tmp = self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i//=2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)


    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize-=1
        self.percDown(1)
        return retval

    def minChild(self, i):
        if (2*i) + 1 > self.currentSize:
            return i*2

        else:
            if self.heapList[2*i+1]>self.heapList[2*i]:
                return 2*i+1

            return 2*i

    def percDown(self, i):
        while i*2 <=self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i]:
                tmp = self.heapList[mc]
                self.heapList[mc]=self.heapList[i]
                self.heapList[i]=tmp
            i=mc


    def buildHeap(self, alist):
        i = len(alist)//2
        self.heapList = [0] + alist
        self.currentSize = len(alist)
        while i>0:
            self.percDown(i)
            i-=1



