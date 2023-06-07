class Node:

    """
    This class's used as base structure for nodes in linked list
    instance variables:
        -> data = data to be held by node
        -> next = keeps track of next node its connected to, its None if its not connected
    methods:
        have used dunder/magical methods like init and str but 
        logically no methods are used
        __str__ -> used for printing data without using .data notation in print function
        __repr__ -> is the representation of node
    """

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return F"Node holding value {self.data}"


