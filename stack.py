#impleenting stack without inbuilt functions
class Stack:    
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def display(self):
        print(self.stack)
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
print("Size of stack: ", s.size())
print("Popped element: ", s.pop())
print("Popped element: ", s.pop())
print("Popped element: ", s.pop())
print("Popped element: ", s.pop())
print("Popped element: ", s.pop())
s.display()
print("Size of stack: ", s.size())
print("Peek element: ", s.peek())

