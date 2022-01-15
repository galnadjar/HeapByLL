import sys

from linkedList import LinkedList
from node import Node


class SortedList(LinkedList):
    def __init__(self):
        super().__init__()

    # complexity O(n)
    def insert(self, value):
        if self.size == 0:                                #case its the first element
            self.head.set_val(value)
            self.size += 1

        else:
                curr = self.head
                prev = curr
                while curr is not None:

                    if curr.val == value: #means its exist
                        return

                    elif curr.val < value:
                        prev = curr
                        curr = curr.get_next()

                    else:
                        temp = Node(value, curr)

                        if curr == self.head:               #case its the smallest number move the head to it
                            self.head = temp

                        else:                               #case its number in between we set the previous to it
                            prev.set_next(temp)

                        self.size += 1
                        return

                temp = Node(value)                          #case its the biggest number its connected to the last
                prev.set_next(temp)
                self.size += 1


    # complexity O(1)
    def extract_min(self):
        val = self.get_head().get_val()
        self.head = self.head.get_next()
        self.size -= 1
        return val

    #complexity O(1)
    def minimum(self):
        if self.size > 0:
            return self.head.get_val()
        return "Does Not exist because heap is empty"

    #complexity o(n)
    def union(self, B):
        if self.size == 0:
            return B

        else:

            dummylinkedLst = SortedList()
            currDummy = None
            currA = self.get_head()
            currB = B.get_head()
            Aval = sys.maxsize
            Bval = sys.maxsize

            while currA or currB:

                    temp = Node()
                    if not currB or (currA and currA.get_val() < currB.get_val()):
                        Aval = currA.get_val()
                        temp.set_val(Aval)
                        currA = currA.get_next()

                    elif not currA or (currB and currB.get_val() <= currA.get_val()):
                        Bval = currB.get_val()
                        temp.set_val(Bval)
                        currB = currB.get_next()

                    if dummylinkedLst.get_head().get_val() is None:
                        dummylinkedLst.set_head(temp)
                        currDummy = dummylinkedLst.get_head()
                        dummylinkedLst.size += 1


                    elif currDummy.get_val() != Aval and currDummy.get_val() != Bval:
                            currDummy.set_next(temp)
                            currDummy = currDummy.get_next()
                            dummylinkedLst.size += 1

                    Aval = sys.maxsize
                    Bval = sys.maxsize

        return dummylinkedLst
