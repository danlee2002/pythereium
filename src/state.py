from stack import Stack
from storage import Storage
from memory import Memory
class StateMachine:
    def __init__(self):
        self.memory = Memory()
        self.stack = Stack()
        self.storage = Storage()
