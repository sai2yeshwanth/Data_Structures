from collections import deque
 
queue = deque()
 
# Adding elements to a queue
queue.append('one')
queue.append('two')
queue.append('three')
 
print(queue)
 

print(queue.popleft()) #removeing element using popleft 
print(queue.popleft())
print(queue.popleft())
 
print(queue)