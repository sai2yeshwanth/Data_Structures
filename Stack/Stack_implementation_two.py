 
from collections import deque
 
stack = deque()
 

stack.append('one')
stack.append('two')
stack.append('two')
 
print('Initial stack:')
print(stack)
 

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)    
#print(stack.pop()) #index error (there no elements in stack)