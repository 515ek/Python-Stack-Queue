#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question4: Implement a transfer function and two temporary stacks, to replace the contents of a given stack S with
## those same elements, but in reverse order.
#####################################################################################################################
import user_ds as UDS
import random
def transfer(S):
    T1 = UDS.unlimStack()
    T2 = UDS.unlimStack()
    while not S.isEmpty():
        T1.push(S.pop())
    while not T1.isEmpty():
        T2.push(T1.pop())
    while not T2.isEmpty():
        S.push(T2.pop())
    return S.data

def seed_stack(stk):
    for i in range(10):
        stk.push(random.randint(i*3,(i+1)*3))
    return stk.data

def Soln04():
    S = UDS.unlimStack()
    assert(S.isEmpty())
    T = UDS.unlimStack()
    assert(T.isEmpty())
    st = list(seed_stack(S))
    assert(S.stackPeek())
    return (st,transfer(S))

if __name__ == '__main__':
    print(Soln04())