from stack import Stack
from typing import List 
class Memory:
    def __init__(self):
        self.mem: List[int] = []
    
    def mstore8(self, loc: int, stack: Stack):
        mem_size = len(self.mem)
        bit_mask = 0xFF
        value = stack.peek() & bit_mask 
        stack.pop()
        if mem_size <= loc:
            self.resize(loc - mem_size + 1)
        self.mem[loc] = value

    def mstore(self, loc: int, val: int):
        mem_size = len(self.mem)
        if mem_size <= (loc + 31):
            self.resize(loc - mem_size + 32)
        if val > (1 << 257) -1  or val < 0:
            raise ValueError("val must be unsigned 8 byte value")
        for i in range(32):
            self.mem[loc + i] = (val >> 8 * (31 - i))
    
    def mload(self, loc: int, stack: Stack):
        if (loc + 31) >= len(self.mem):
            raise IndexError("Index out of bounds error")
        val = 0
        for i in range(32):
            val = (val <<  8 * i) | self.mem[loc + i]
        stack.push(val)

    
    def resize(self, bytes: int):
        for i in range(bytes):
            self.mem.append(0)
    
        
        
    
    