from unsortedList import UnSortedList
from node import Node
import sys

class ForeignList(UnSortedList):
    classElements = set()

    def __init__(self):
        super().__init__()
        self.elements = self.classElements


    #O(1) complexity
    def union(self, B):
        if self.size == 0:
            return B

        else:
            self.min = min(self.min, B.min)
            self.prevMin = min(self.prevMin, B.prevMin)
            self.tail.set_next(B.get_head())
            self.size = self.get_size() + B.get_size()
            return self
