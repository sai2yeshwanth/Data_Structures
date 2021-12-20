class Queue:
    class Node:
         def __init__(self,data,next):
             self.data = data
             self.next = next

    def __init__(self):
        self.head = None
        self.tail =None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new = self.Node(data, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is Empty")
        result = self.head.data
        self.head = self.head.next
        self.size -=1
        if self.is_empty():
            self.tail = None
        return result

    
    def first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self.head.data

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print()
if __name__ == '__main__':

    lq = Queue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    lq.enqueue(40)

    lq.print()

    print("popped :",lq.dequeue())

    lq.print()
    lq.enqueue(700)

    lq.print()
    
    print("Top data:", lq.first())
