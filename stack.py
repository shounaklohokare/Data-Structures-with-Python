#This Python program demonstrates implementation of Stack Data Structure.

class Stack(object):

    def __init__(self):
        self.dataitems = []

    def isEmpty(self):
        return self.dataitems==[]

    def push(self, item):
        self.dataitems.append(item)

    def pop(self):
        return self.dataitems.pop()

    def peek(self):
        return self.dataitems[-1]

    def size(self):
        return len(self.dataitems)

    def __str__(self):
        if self.isEmpty():
            return 'Stack is Empty'

        else:
            for element in enumerate(self.dataitems):
                print(element)


stack = Stack()

