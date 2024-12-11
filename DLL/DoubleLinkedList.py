class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None



class DoublyLinkedList:
    def __init__(self , value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self , value):
       new_node = Node(value)

       if self.head is None :
           self.head = new_node
           self.tail = new_node
       else :
           self.tail.next = new_node
           new_node.prev = self.tail
           self.tail = new_node

       self.length +=1

    def pop(self):
       if self.length == 0 :
           return None

       temp = self.tail

       if self.length == 1 :
           self.head = None
           self.tail = None
       else :
           self.tail = temp.prev
           self.tail.next = None
           temp.prev = None

       self.length -= 1
       return temp



    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = None
        if index <= self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next

        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp


    def set_value(self , index , value):
       new_node = self.get(index)
       if new_node is None:
           return False
       new_node.value = value
       return True


    def insert(self , index , value):
        if index < 0 or index > self.length:
            return False

        if index == 0 :
            self.prepend(value)
            return True
        if index == self.length :
            self.append(value)
            return True
        new_node = Node(value)
        temp = self.get(index)
        pre = temp.prev
        new_node.next = temp
        temp.prev = new_node
        pre.next = new_node
        new_node.prev = pre
        self.length +=1
        return True


    def remove(self , index ):
        if index < 0 or index >= self.length:
            return False

        temp = None
        if index == 0:
            temp = self.pop_first()
            return temp
        if index == self.length - 1:
            temp = self.pop()
            return temp

        temp = self.get(index)

        pre = temp.prev
        pre.next = temp.next
        temp.next.prev = pre

        temp.next = None
        temp.prev = None
        self.length -= 1

        return temp



