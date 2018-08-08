#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question1: Implement a function with signature transfer(S,T) that transfers all elements from Stack S onto Stack T,
## so that, elements that starts at the top of S is the first to be inserted into T, and element at the bottom of 
## S ends up at the top of T.
######################################################################################################################
import user_ds as UDS
import random
def transfer(S,T):
    while not S.isEmpty():
        T.push(S.pop())
        print
    return T.data

def seed_stack(stk):
    for i in range(10):
        stk.push(random.randint(i*3,(i+1)*3))
    return stk.data

def Soln01():
    S = UDS.unlimStack()
    assert(S.isEmpty())
    T = UDS.unlimStack()
    assert(T.isEmpty())
    st = list(seed_stack(S))
    assert(S.stackPeek())
    return (st,transfer(S,T))

if __name__ == '__main__':
    print(Soln01())