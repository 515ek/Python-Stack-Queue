#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question 7. Design a stack using a single queue as an instance variable, and only constant additional local memory within the method bodies.
#####################################################################################################################
import user_ds as uds

class qStack():
    def __init__(self):
        self.data = uds.flexQueue()
    
    def isEmpty(self):
        return self.data.isEmpty()

    def stackLength(self):
        return self.data.qLength()
    
    def stackPeek(self):
        pass
    
    def push(self,item):
        self.data.enque(item)
    
    def pop(self):
        if not self.data.isEmpty():
            i = 1
            while i < self.data.qLength():
                self.data.enque(self.data.deque())
                i += 1
            return self.data.deque()
        else:
            return False

def test_soln07():
    qs = qStack()
    assert(qs.isEmpty())
    qs.push(2)
    qs.push(3)
    qs.push(4)
    qs.push(5)
    qs.push(6)
    return qs.pop()

if __name__ == '__main__':
    print(test_soln07())