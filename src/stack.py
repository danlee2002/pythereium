
from typing import List 
class Stack:
    def _init__(self):
        self.stack: List[int] = []
        self.MAX_STACK_SIZE: int = 1024

    def push(self,value: int):
        if len(self.stack) == self.MAX_STACK_SIZE:
            raise MemoryError("Stack Overflow")
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == self.MAX_STACK_SIZE:
            raise IndexError("Stack Underflow")
        self.stack.pop()

    def swap(self):
        temp = self.stack[-1]
        self.stack[-1] = self.stack[-2]
        self.stack[-2] = temp 

    def dup(self):
        if len(self.stack) == 0:
            raise IndexError("Cannot dup on an empty stack")
        self.stack.append(self.stack[-1])
    
    def add(self):
        if len(self.stack) < 2:
            raise IndexError("Cannot add on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand + operand1)

    def sub(self):
        if len(self.stack) < 2:
            raise IndexError("Cannot sub on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand - operand1)

    def mul(self):
        if len(self.stack) < 2:
            raise IndexError("Cannot mul on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand * operand1)
    
    def div(self):
        if len(self.stack) < 2:
            raise IndexError("Cannot div on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand // operand1)
    
    def mod(self):
        if len(self.stack)< 2:
            raise IndexError("Cannot mod on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand % operand1)
    
    def _and(self):
        if len(self.stack)< 2:
            raise IndexError("Cannot and on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand & operand1)

    def _or(self):
        if len(self.stack)< 2:
            raise IndexError("Cannot or on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand | operand1)
    
    def _xor(self):
        if len(self.stack)< 2:
            raise IndexError("Cannot xor on stack with less than 2 elements")
        operand = self.stack.pop()
        operand1 = self.stack.pop()
        self.stack.append(operand ^ operand1)
    
    def _neg(self):
        if len(self.stack) == 0:
            raise IndexError("Cannot neg on stack with less than 2 elements")
        bit_mask = (1 << 257) - 1 
        self.stack[-1] = (bit_mask & ~self.stack[-1])
