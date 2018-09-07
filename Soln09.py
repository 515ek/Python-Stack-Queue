#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 07-09-2018
## Assignment: Stacks and Queues
## Question 9. Design a double-ended queue using two stacks as instance variables.
#####################################################################################################################
import user_ds as uds 
class DQueue:
    def __init__(self):
        self.front = uds.unlimStack()
        self.back = uds.unlimStack()
    
    def isEmpty(self):
        return self.front.isEmpty() and self.back.isEmpty()
    
    def qLength(self):
        return self.front.stackLength() + self.back.stackLength()
    
    def enqueFront(self,val):
        self.front.push(val)
    
    def enqueBack(self,val):
        self.back.push(val)
    
    def dequeFront(self):
        if not self.front.isEmpty():
            return self.front.pop()
        elif not self.back.isEmpty():
            while not self.back.isEmpty():
                self.front.push(self.back.pop())
            else:
                ele = self.front.pop()
            while not self.front.isEmpty():
                self.back.push(self.front.pop())
            return ele
    
    def dequeBack(self):
        if not self.back.isEmpty():
            return self.back.pop()
        elif not self.front.isEmpty():
            while not self.front.isEmpty():
                self.back.push(self.front.pop())
            else:
                ele = self.back.pop()
            while not self.back.isEmpty():
                self.front.push(self.back.pop())
            return ele


def test_soln09():
    stdq = DQueue()
    assert(stdq.isEmpty())
    stdq.enqueFront(10)
    stdq.enqueFront(20)
    stdq.enqueBack(30)
    stdq.enqueBack(40)
    assert(stdq.qLength() == 4)
    assert(stdq.dequeBack() == 40)
    assert(stdq.dequeFront() == 20)
    assert(stdq.dequeFront() == 10)
    assert(stdq.dequeFront() == 30)
    assert(stdq.qLength() == 0)
    stdq.enqueFront(10)
    stdq.enqueFront(20)
    assert(stdq.dequeBack() == 10)
    assert(stdq.dequeBack() == 20)

if __name__ == '__main__':
    test_soln09()