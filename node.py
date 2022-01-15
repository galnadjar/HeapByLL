class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

