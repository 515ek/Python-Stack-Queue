#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Implementing the Stack DataStructure
## Question: Create a Class myStack to implement the working of Stack DataStructure.
######################################################################################

class myStack:
    capacity = 5
    def __init__(self):
        self.data = []
        self.count = 0
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count >= myStack.capacity

    def stackLength(self):
        return self.count

    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return False
    
    def push(self,dat):
        if not self.isFull():
            self.data.append(dat)
            self.count += 1
    
    def pop(self):
        if not self.isEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return False

class unlimStack:
    def __init__(self):
        self.data = []
        self.count = 0
        
    def isEmpty(self):
        return self.count == 0
    
    def stackLength(self):
        return self.count

    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return False
    
    def push(self,dat):
        self.data.append(dat)
        self.count += 1
    
    def pop(self):
        if not self.isEmpty():
            self.count -= 1
            return self.data.pop()

'''
class singleQueue():
    cap = 20

    def __init__(self):
        self.data = []
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.rear == singleQueue.cap
    
    def queueLength(self):
        return self.rear
    
    def insert(self,item):
        if not self.isFull():
            self.data.append(item)
            self.rear += 1
    
    def remove(self):
        if not self.isEmpty():
            tmp = self.data[self.front]
            self.data.remove(tmp)
            self.rear -= 1
            return tmp
'''

class flexQueue():
    cap = 4
    def __init__(self):
        self.data = [None] * flexQueue.cap
        self.front = 0
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def qLength(self):
        return self.size
    
    def qCapacity(self):
        return len(self.data)
    
    def qFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
    
    def deque(self):
        if not self.isEmpty():
            element = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % len(self.data)
            self.size -= 1
            """ if 0 < self.size < len(self.data) // 4:
                self.resize(len(self.data)//2) """
            return element
        else:
            return None
    
    def enque(self, item):
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        new_pos = (self.front + self.size) % len(self.data)
        self.data[new_pos] = item
        self.size += 1
    
    def resize(self, cap):
        old = self.data
        walk = self.front
        self.data = [None] * cap
        for k in range(len(old)):
            #print(walk,k,len(self.data),len(old))
            self.data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self.front = 0
    