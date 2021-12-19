class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #Address of NextNode

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"--->", end =" ")
                temp = temp.next

L = SingleLinkedList() #empty List
n1 = Node(10)
L.head = n1 #n1 = L
n2 = Node(20)
n1.next = n2 #n2 =n1
n3 = Node(30)
n2.next = n3 #n3= n2 
n4 = Node(40)
n3.next =n4 #n4 = n3
L.display()


        