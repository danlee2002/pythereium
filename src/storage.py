from stack import Stack
class Storage:
    def __init__(self):
        self.slot = {}

    def sload(self, loc: int, stack: Stack):
        if loc > (1 << 257) - 1 or loc < 0:
            raise IndexError("loc must be u256 value")
        if loc in self.slot:
            stack.push(self.slot[loc])
        else:
            stack.push(0)
            self.slot[loc] = 0

    def sstore(self, loc: int, val: int):
        if loc > (1 << 257) -1 or loc < 0:
            raise IndexError("loc must be u256 value")
        if val > (1 << 257) -1 or val < 0:
            raise ValueError("loc must be u256 value")
        # implement warm/code slot 
        self.slot[loc] = val
    

        
