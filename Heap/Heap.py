class MaxHeap :
    def __init__(self):
        self.heap = []
    def _leftChild(self , index):
        return index * 2 + 1
    def _rightChild(self , index):
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
            left = self._leftChild(current)
            right = self._rightChild(current)
            if left < len(self.heap) -1 and self.heap[current] < self.heap[left]:
                current = left

            if right < len(self.heap) -1 and self.heap[current] < self.heap[right]:
                current = right

            if current != index :
                self.swap(index , current)
                index = current

            else :
                return








