#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question3: Modify ArrayStack implementation so that the stack’s capacity is limited to maxlen elements. If push is
## called when the stack is at full capacity, throw a Full exception.
######################################################################################################################
import user_ds as uds
import sys
import random
class ArrayStack(uds.myStack):

    def __init__(self,mlen):
        super().__init__()
        uds.myStack.capacity = mlen
    
    def push(self,dat):
        if self.isFull():
            StackFull = Exception()
            raise StackFull
        else:
            self.data.append(dat)
            self.count += 1

def seed_stack(stk):
    for i in range(stk.capacity):
        stk.push(random.randint(i*3,(i+1)*3))
    return stk.data

def Soln03():
    astk = ArrayStack(5)
    seed_stack(astk)
    astk.push(5)

if __name__ == '__main__':
    Soln03()