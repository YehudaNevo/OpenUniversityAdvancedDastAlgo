class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.parent(i) >= 0

    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while self.has_parent(i) and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        while self.has_left_child(i):
            smaller_child_index = self.left_child(i)
            if self.has_right_child(i) and self.heap[self.right_child(i)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(i)

            if self.heap[i] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(i, smaller_child_index)
            i = smaller_child_index


min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)

print("Min value:", min_heap.remove_min())
print("Next min value:", min_heap.remove_min())
