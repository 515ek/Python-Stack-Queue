#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question 6: Suppose you have three nonempty stacks R, S and T. Describe a sequence of operations that results in S storing all elements originally in T below of S’s original elements, with both sets of those elements in their original configuration. For example, if R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9], the final configuration should have R = [1, 2, 3] and S = [6, 7, 8,  9, 4, 5].
#####################################################################################################################
import user_ds as uds
import random

def seed_stack(stk,cap):
    for i in range(cap):
        stk.push(random.randint(i*3,(i+1)*3))
    return stk.data

def sequence(R,S,T):
    count = R.stackLength()
    while not S.isEmpty():
        R.push(S.pop())
    while not T.isEmpty():
        R.push(T.pop())
    while R.stackLength() > count:
        S.push(R.pop())
    return (R.data,S.data)


def soln06():
    R = uds.unlimStack()
    S = uds.unlimStack()
    T = uds.unlimStack()
    seed_stack(R,3)
    seed_stack(S,6)
    seed_stack(T,4)
    ans = T.data + S.data
    return (R.data,ans),sequence(R,S,T)

if __name__ == '__main__':
    print(soln06())