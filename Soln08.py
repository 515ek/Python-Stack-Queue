#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 07-09-2018
## Assignment: Stacks and Queues
## Question 8. Design a queue using two stacks as instance variables, such that all queue operations execute in amortized O(1) time.
#####################################################################################################################
import user_ds as uds 
class StkQueue:
    def __init__(self):
        self.data = uds.unlimStack()
        self.tmp = uds.unlimStack()
    
    def isEmpty(self):
        return self.data.isEmpty()
    
    def qLength(self):
        return self.data.stackLength()
    
    def enque(self,val):
        self.data.push(val)
    
    def deque(self):
        while not self.data.isEmpty():
            self.tmp.push(self.data.pop())
        else:
            ele = self.tmp.pop()
        while not self.tmp.isEmpty():
            self.data.push(self.tmp.pop())
        return ele

def test_soln09():
    stdq = StkQueue()
    assert(stdq.isEmpty())
    stdq.enque(10)
    stdq.enque(20)
    stdq.enque(30)
    stdq.enque(40)
    assert(stdq.qLength() == 4)
    assert(stdq.deque() == 10)
    assert(stdq.deque() == 20)
    assert(stdq.deque() == 30)
    assert(stdq.deque() == 40)
    assert(stdq.qLength() == 0)

if __name__ == '__main__':
    test_soln09()