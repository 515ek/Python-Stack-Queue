#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question2: Implement a function that reverses a list of elements by pushing them onto a stack in one order, and 
## write them back to the list in reversed order.
#####################################################################################################################
import user_ds as uds
import random

def seed(ls):
    for i in range(10):
        ls.append(random.randint(i*4,(i+1)*4))
    return ls

def reversed_list(ls):
    stk = uds.unlimStack()
    for i in range(len(ls)):
        stk.push(ls[i])
    ls = []
    while not stk.isEmpty():
        ls.append(stk.pop())
    return ls

def Soln02():
    ls = []
    tmp = list(seed(ls))
    return (tmp,reversed_list(ls))

if __name__ == '__main__':
    print(Soln02())
