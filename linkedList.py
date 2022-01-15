from node import Node
import sys
class LinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0
        self.min = sys.maxsize
        self.prevMin = sys.maxsize

    #removing the head of the list and returning its value
    def pop(self):
        val = self.get_head().get_val()
        self.head = self.head.get_next()
        self.size -= 1
        return val

    #printing the heap
    def print(self):
        curr = self.head
        print("Heap state: ", end="")

        if self.size == 0:
            print("Empty")

        else:
            while curr is not None:
                val = curr.get_val()
                print(" [" + str(val), end="] ->")
                curr = curr.get_next()
            print("|")

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def set_head(self, node):
        self.head = node

