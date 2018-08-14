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
            if stk.stackPeek()[1:-1] == symbol[2:-1]:
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
    print(stk.data)
    return stk.isEmpty()

def parse(script):
    stk = uds.unlimStack()
    start = script.find('<')
    while start != -1:
        end = script[start:].find('>') + start
        print('end-->',script[end:])
        tag = script[start+1:end]
        print('tag-->',tag)
        if tag[0] != '/' and tag[-1] != '/':
            stk.push(tag.split(' ')[0])
        elif tag[0] != '/' and tag[-1] == '/':
            if not validate('<'+tag+'>'):
                return False
        elif stk.stackPeek() == tag[1:]:
            stk.pop()
        script = script[end+1:]
        print('script-->',script)
        start = script.find('<')
        print('start-->','\''+script[start:])
    return stk.isEmpty()

def Soln05(tag):
    return(parse(tag))

if __name__ == '__main__':
    print(Soln05('<html> <body> <font color = \'red\' /> </body> </html>'))