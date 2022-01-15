import sys
from linkedList import LinkedList
from node import Node


class UnSortedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None
        self.elements = set()

        # complexity O(1)

    def minimum(self):
        if self.size > 0:
            return self.min
        return "Does Not exist because heap is empty"

    #complexity O(1)
    def insert(self, value):

        if self.size == 0:  # case its the first element
            self.head.set_val(value)
            self.tail = self.head
            self.size += 1

        elif not self.elements.__contains__(value):
            temp = Node(value, self.head)
            self.head = temp
            self.size += 1

        self.min = min(self.min, value)
        self.elements.add(value)


        if self.size > 1 and value != self.min:
            self.prevMin = min(self.prevMin, value)


    # complexity O(n)
    def extract_min(self):

        if self.size > 0:

            curr = self.get_head()
            minValLocPrev = curr
            minToRemove = self.min

            while curr.get_next() is not None:
                if curr.get_next().get_val() == minToRemove:
                    minValLocPrev = curr
                else:
                    self.prevMin = min(self.prevMin, curr.get_next().get_val())
                curr = curr.get_next()

            if minValLocPrev == self.get_head():  # case the min is the head or adjacent to it

                if minToRemove != self.get_head().get_val():  # min val is adjacent to head and not the actual head
                    temp = self.get_head().get_next()
                    self.head.set_next(temp.get_next())

                else:
                    self.head = self.head.get_next()

            elif minValLocPrev.get_next() == curr:  # case the min is the tail
                minValLocPrev.set_next(None)
                self.tail = minValLocPrev

            else:  # case the min is in-between nodes
                minValLocPrev.set_next(minValLocPrev.get_next().get_next())

            self.size -= 1

            if self.size == 0:
                self.head = Node()

            elif self.size == 1:
                self.min = self.get_head().get_val()
                self.tail = self.head

            else:
                self.min = self.prevMin
                self.prevMin = sys.maxsize

            self.elements.discard(minToRemove)
            return minToRemove


    # average complexity O(m) where m is the size of B
    def union(self, B):

        if self.size == 0:
            self.elements = B.elements
            return B

        else:
            while B.get_size() > 0:
                item = B.pop()
                if item < self.minimum():
                    self.min = item
                else:
                    self.prevMin = min(self.prevMin, item)
                B.elements.discard(item)
                self.insert(item)
            return self

