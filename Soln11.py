#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 09-09-2018
## Assignment: Stacks and Queues
## Question 11. In certain applications of the queue, it is common to repeatedly dequeue an element, process it in some way, and then immediately enqueuer the same element. Modify ArrayQueue implementation to include a rotate( ) method that has semantics identical to the combination, Q.enqueue (Q.dequeue()). However, your implementation should be more efficient than making two separate calls.
#####################################################################################################################

import user_ds as uds 

class ArrayQueue(uds.flexQueue):

    def __init__(self):
        super().__init__()
    
    def rotate(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % len(self.data)
            while self.data[self.front] == None:
                self.front = (self.front + 1) % len(self.data)

def test11():
    q = ArrayQueue()
    ls = [2,3,5,6]
    for l in ls:
        q.enque(l)
    print(q.qFirst())
    print(q.deque())
    q.rotate()
    print(q.qFirst())
    q.rotate()
    print(q.qFirst())
    q.rotate()
    print(q.qFirst())

if __name__ == '__main__':
    test11()