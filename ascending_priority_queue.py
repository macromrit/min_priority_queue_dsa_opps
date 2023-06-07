# importing base structure of node which was designed in file node_models
from node_models import Node


class MinPriorityQueue: # an ascending priority queue is called as min priority queue as well
    
    def __init__(self) -> None:
        self.priority_head = None
        self.tail = None # to make enqueuing in O(1) time complexity

    def enqueue(self, data) -> bool: # type hinting
        try:
            node = Node(data) # initializing node with data provided

            # if tail is none then its an empty list
            if not self.tail:
                self.priority_head = self.tail = node
            else:
                # achieving the process of enqueuing at O(1) by using attribute/instance-variable tail
                self.tail.next = node
                self.tail = self.tail.next
        except: # if any error/exception's catched
            return False
        else: # if no errors detected, process was a success
            return True



    def dequeue(self) -> Node or str: # type hinting
        try:
            prev, node = self.findMinRtrnPrev()
            
            if not prev: # then head's the node with lowest value in LIST
                self.priority_head = self.priority_head.next
            else:
                prev.next = prev.next.next # replacing prev's next to min node's next so that min node can be removed from the list
            
            return node
        
        except:
            return "Underflow Exception was hit!!!"
            

    def findMinRtrnPrev(self) -> tuple: 
        # motive is to figure out min node of the list and return it and previous node to it
        
        # if its an emtpy list then raise Exception
        if not self.priority_head:
            raise Exception("Empty List aren't considered")
        
        min_prev = None
        prev = None
        min_node = self.priority_head
        curr = self.priority_head

        while curr:
            if curr.data<min_node.data:
                min_prev = prev
                min_node = curr
            prev = curr
            curr = curr.next
        
        return min_prev, min_node # returning min node and the previous node to it in a tuple

    
    def peak(self) -> str or int:
        # the node with lowest value would be dequeed in further proceedings... 
        # so the one which has lowest value must be displayed without professing removal operation on it.
        try:
            return self.findMinRtrnPrev()[1]
        except:
            return"There's no use in peeking an empty list!!!"



    def display(self):
        # displaying the queue as in the specified format

        curr = self.priority_head
        print("front", sep="", end=" -> ")
        while curr:
            print(curr, end=" -> ")
            curr = curr.next

        print("rear")


if __name__=="__main__":
    
    # test case 

    queue = MinPriorityQueue()
    queue.enqueue(5)
    queue.enqueue(1)
    queue.enqueue(6)
    queue.enqueue(-6)
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue()) # for hitting underflow exception
    print(queue.peak())
    queue.display()
    
