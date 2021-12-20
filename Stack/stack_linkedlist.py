class Stack:
    class Node:
         def __init__(self,data,next):
             self.data = data
             self.next = next
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, new_e):
        self.head = self.Node(new_e,self.head)
        self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        value = self.head.data
        self.head = self.head.next
        self.size -=1
        return value
    
    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.head.data

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print()
if __name__ == '__main__':

    ls = Stack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    ls.push(40)

    ls.print()

    print("popped :",ls.pop())

    ls.print()
    ls.push(700)

    ls.print()
    
    print("Top data:", ls.top())

