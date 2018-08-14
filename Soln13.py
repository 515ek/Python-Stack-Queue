#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question 13: Implement LeakyStack. This stack should be of fixed size. When push is invoked with the stack at full capacity, rather than throwing a Full exception, accept the pushed element at the top while “leaking” the oldest element from the bottom of the stack to make a room.
######################################################################################################################
import user_ds as uds
import sys
import random
class LeakyStack(uds.myStack):
    def __init__(self):
        super().__init__()
    
    def push(self,dat):
        if self.isFull():
            self.data.remove(self.data[0])
            self.data.append(dat)
        else:
            self.data.append(dat)
            self.count += 1

def seed_stack(stk):
    for i in range(stk.capacity):
        stk.push(random.randint(i*3,(i+1)*3))
    return stk.data

def Soln13():
    lstk = LeakyStack()
    seed_stack(lstk)
    print(lstk.data)
    lstk.push(5)
    print(lstk.data)
    lstk.push(10)
    print(lstk.data)

if __name__ == '__main__':
    Soln13()