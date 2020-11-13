
class MinimumBinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self, i):
        while i//2>0:
            if self.heapList[i//2]>self.heapList[i]:
                temp = self.heapList[i//2]
                self.heapList[i]=self.heapList[i//2]
                self.heapList[i//2]=temp
            i//=2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)

    def minChild(self, i):
        if 2*i+1>self.currentSize:
            return 2*i

        else:
            if self.heapList[2*i+1]>self.heapList[2*i]:
                return 2*i

            return 2*i+1

    def percDown(self, i):
        while i*2<=self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc]<self.heapList[i]:
                temp = self.heapList[mc]
                self.heapList[mc]=self.heapList[i]
                self.heapList[i]=temp
            i=mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist)//2
        self.heapList.append(alist)
        self.currentSize = len(alist)

        while i>0:
            self.percDown(i)
            i-=1

