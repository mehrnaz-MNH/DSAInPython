class MaxHeap :
    def __init__(self):
        self.heap = []
    def _left_child(self , index):
        return index * 2 + 1
    def _right_child(self , index):
        return  index * 2 + 2
    def _parent(self , index):
        return (index - 2) // 2
    def _swap(self , index1 , index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]

    def insert(self , value):
        self.heap.append(value)
        cur = len(self.heap) - 1
        while cur > 0 :
            par = self._parent(cur)
            if value > self.heap[par]:
                self._swap(cur , par)
                cur = par
            else :
                break

    def remove(self):
        if len(self.heap) == 0 :
            return None
        if len(self.heap) == 1 :
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap) - 1)
        self.sink_down(0)
        return max_value


    def sink_down(self , index):
        current  = index
        while True :
            left = self._left_child(current)
            right = self._right_child(current)
            if left < len(self.heap)  and self.heap[current] < self.heap[left]:
                current = left

            if right < len(self.heap) and self.heap[current] < self.heap[right]:
                current = right

            if current != index :
                self._swap(index , current)
                index = current

            else :
                return

myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)


"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""

class MinHeap :
    def __init__(self):
        self.heap = []
    def _left_child(self , index):
        return index * 2 + 1
    def _right_child(self , index):
        return  index * 2 + 2
    def _parent(self , index):
        return (index - 2) // 2
    def _swap(self , index1 , index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]

    def insert(self , value):
        self.heap.append(value)
        cur = len(self.heap) - 1
        while cur > 0 :
            par = self._parent(cur)
            if value < self.heap[par]:
                self._swap(cur , par)
                cur = par
            else :
                break

    def remove(self):
        if len(self.heap) == 0 :
            return None
        if len(self.heap) == 1 :
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap) - 1)
        self.sink_down(0)
        return max_value


    def sink_down(self , index):
        current  = index
        while True :
            left = self._left_child(current)
            right = self._right_child(current)
            if left < len(self.heap)  and self.heap[current] > self.heap[left]:
                current = left

            if right < len(self.heap) and self.heap[current] > self.heap[right]:
                current = right

            if current != index :
                self._swap(index , current)
                index = current

            else :
                return











