class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print()

    def get_length(self):  #length of the list
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data): #insert data at begining
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):  #insert data at end
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):   #addind data in list(before index)
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):  #remove data 
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list): #creating a new linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_at(1,"blueberry")
    ll.print()
    ll.remove_at(2)
    ll.print()
    

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()

    llist = LinkedList() 
    llist.insert_values(["one","two","three"])
    llist.print()

    ll.print()