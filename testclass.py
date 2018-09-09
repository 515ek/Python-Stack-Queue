#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Test file for implemented classes
## Question: test the Class myStack(implemented the working of Stack DataStructure).
######################################################################################
import user_ds as UDS
import random

def test_stack_empty():
    stk = UDS.myStack()
    ustk = UDS.unlimStack()
    assert(stk.isEmpty())
    assert(stk.stackLength()==0)
    assert(ustk.isEmpty())
    assert(ustk.stackLength()==0)

def test_stack_full():
    stk = UDS.myStack()
    for el in range(UDS.myStack.capacity):
        assert(not stk.isFull())
        stk.push(random.randint(el,el*5))
    assert(stk.isFull() == True)
    assert(stk.stackPeek())
    assert(stk.pop())
    assert(stk.stackPeek())

def test_unlimStack():
    ustk = UDS.unlimStack()
    assert(not ustk.push(random.randint(1,50)))
    assert(not ustk.push(random.randint(1,50)))
    assert(ustk.stackPeek())
    while not ustk.isEmpty():
        assert(ustk.pop())

def test_flexQue():
    fq = UDS.flexQueue()
    assert(fq.isEmpty())
    for i in range(10):
        fq.enque(random.randint(1,50))
    assert(fq.qLength() == 4)
    assert(fq.qFirst())
    assert(fq.qCapacity() == 4)
    fq.enque(random.randint(1,50))
    assert(fq.qLength() == 5)
    assert(fq.qCapacity() > 4)

if __name__ == '__main__':
    test_stack_empty()
    test_stack_full()
    test_unlimStack()
    test_flexQue()