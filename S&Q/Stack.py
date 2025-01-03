class Node :
    def __init__(self , value):
        self.value = value
        self.next = None

class Stack :
    def __init__(self , value):
        self.top = Node(value)
        self.height = 1

    def print_stack(self):
        pointer = self.top
        while pointer is not None :
            print(pointer.value)
            print("|")
            pointer = pointer.next

        print("Top : ", self.top.value)
        print("height : ",self.height)


    def push(self,value):
        new_node = Node(value)
        if self.height != 0 :
            new_node.next = self.top
        self.top = new_node
        self.height +=1
        return True

    def pop(self):
        if self.height == 0 :
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp


my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    1
    2
    3
    4

    Popped node:
    1

    Stack after pop():
    2
    3
    4

"""




