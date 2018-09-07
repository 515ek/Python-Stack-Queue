#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 07-09-2018
## Assignment: Stacks and Queues
## Question 10. Suppose you have a stack S containing n elements and a queue Q that is initially empty. Write function that use Q to scan S to see if it contains a certain element x, with the additional constraint that your algorithm must return the elements back to S in their original order. You may use S, Q and a constant number of other variables.
#####################################################################################################################
import user_ds as uds
import Soln01 as soln


def restore(S,Q):
    i = 1
    while i < Q.qLength():
        Q.enque(Q.deque())
        i += 1
    el = Q.deque()
    print(el)
    return el

def scan(S,x):
    Q = uds.flexQueue()
    while not S.isEmpty():
        el = S.pop()
        if el != x:
            Q.enque(el)
        elif el == x:
            S.push(x)
            while not Q.isEmpty():
                S.push(restore(S,Q))
            return (S.data,True)
    else:
        while not Q.isEmpty():
            S.push(restore(S,Q))
        return(S.data,False)
    
def soln10():
    S = uds.unlimStack()
    S.push(10)
    S.push(20)
    S.push(30)
    print(S.data)
    #S.push(40)
    #S.push(50)
    print(scan(S,10))

if __name__ == '__main__':
    soln10()

