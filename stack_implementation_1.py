stack =[] #creating a empty list

stack.append("One") # append() function to push
stack.append("two")
stack.append("three")

print(stack)

print(stack.pop()) # three is remove form list
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack) #now stack is empty

#print(stack.pop()) #index error (there no elements in stack)
