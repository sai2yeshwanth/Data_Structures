 
from collections import deque
 
stack = deque()
 

stack.append('one')
stack.append('two')
stack.append('two')
 

print(stack)
 


print(stack.pop())
print(stack.pop())
print(stack.pop())


print(stack)    
#print(stack.pop()) #index error (there no elements in stack)