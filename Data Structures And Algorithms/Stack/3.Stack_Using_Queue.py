from queue import LifoQueue
stack = LifoQueue(maxsize=5)
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
print(stack.qsize())
print(stack)
print(stack.full())
print(stack.empty())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack)