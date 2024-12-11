from contextlib import nullcontext


class Node:
    def __init__(self , value):
        self.value = value
        self.next = None



class LinkedList:
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

    # best practice code
    def append(self , value):
        new_node = Node(value)
        if self.head is None :
           self.head = new_node
           self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    # Other way to run it
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.length >= 1 :
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     else:
    #         self.head = new_node
    #         self.tail = new_node
    #     self.length += 1

    def pop(self):
        if self.length == 0 :
            return None
        temp = self.head
        pre = self.head
        while temp.next :
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0 :
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0 :
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0 :
            self.head = None
            self.tail = None
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index+1):
            temp = temp.next

        return temp

    def set_value(self , index , value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self , index , value):
        if index < 0 or index > self.length:
            return False

        if index == 0 :
            self.prepend(value)

        if index == self.length :
            self.append(value)

        new_node = Node(value)
        pre = self.get(index - 1 )
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True

    def remove(self , index ):
        if index < 0 or index >= self.length:
            return None

        if index == 0 :
            self.pop_first()

        if index == self.length -1  :
            self.pop()

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


    def reverse(self):
        # switch head and tail :
        temp = self.head
        self.head = self.tail
        self.tail = temp
        #add more variables
        after = temp.next
        before = None
        # iterate and reverse
        for _ in range (self.length ):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
         




my_LL = LinkedList(11)
my_LL.append(3)
my_LL.append(23)
my_LL.append(7)


my_LL.reverse()
my_LL.print_list()





















