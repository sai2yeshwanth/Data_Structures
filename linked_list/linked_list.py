class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #Address of Next Node

class LinkedList:  #creating a linked List
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print()

L = LinkedList() #empty List
n1 = Node(10)
L.head = n1 #n1 = L
n2 = Node(20)
n1.next = n2 #n2 =n1
n3 = Node(30)
n2.next = n3 #n3= n2
n4 = Node(40)
n3.next =n4 #n4 = n3
L.print()
