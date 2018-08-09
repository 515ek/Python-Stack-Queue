#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Stacks and Queues
## Question5. HTML generally allows optional attributes to be expressed as part of an opening tag. The general form
## used is <name attribute1 = “value1” attribute2 = “value2”>. Write function that checks whether tags or matched
## properly, even when an opening tag may include one or more attributes.
#####################################################################################################################
import user_ds as uds
import sys
def validate(tag):
    symbols = list(tag.split(' '))
    stk = uds.unlimStack()

    ## Remove extra whitespaces from string
    for sym in symbols:
        if sym == '':
            symbols.remove(sym)
    
    ## check symbols of string and validate
    for symbol in symbols:
        if symbol[0] == '<' and not symbol[1] == '/':
            if stk.isEmpty():
                stk.push(symbol)
        elif symbol == '=':
            if stk.stackPeek()[0] != '<':
                stk.push(symbol)
        elif symbol == '/>':
            if stk.stackPeek()[0] == '<':
                stk.pop()
        elif symbol == '>':
            if stk.stackPeek()[0] == '<':
                tmp = stk.pop() + symbol
                stk.push(tmp)
        elif symbol[0:2] == '</' and symbol[-1] == '>':
            if stk.stackPeek()[0] == '<':
                stk.pop()
        else:
            if stk.stackPeek() == '=':
                stk.pop()
                stk.pop()
            elif stk.stackPeek() == '<':
                tmp = stk.pop() + symbol
                stk.push(tmp)
            else:
                stk.push(symbol)
    return stk.isEmpty()

def Soln05(tag):
    return(validate(tag))

if __name__ == '__main__':
    print(Soln05('<font color = \'red\' />'))