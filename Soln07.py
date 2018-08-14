#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question 7. Design a stack using a single queue as an instance variable, and only constant additional local memory within the method bodies.
#####################################################################################################################
import user_ds as uds

class qStack():
    def __init__(self):
        self.data = uds.singleQueue()
    
    def isEmpty(self):
        self.data.isEmpty()
    
    def isFull(self):
        self.data.isFull()

    def stackLength(self):
        self.data.queueLength()
    
    def stackPeek(self):
        pass
    
    def push(self,item):
        pass
    
    def pop(self):
        pass