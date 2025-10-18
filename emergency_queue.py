# "class Patient":

#   def __init__(self, name, urgency):
#       self.name = name
#       self.urgency = urgency  # 1 is most urgent (min value)

#   def __repr__(self):
#        return f"{self.name} ({self.urgency})"



# "class MinHeap":

#    def __init__(self):
#       self.data = []

#    def heapify_up(self, index):
#        """Move the patient up until the heap property is restored."""
#        parent_index = (index - 1) // 2
#        while index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
#            index = parent_index
#            parent_index = (index - 1) // 2

#    def heapify_down(self, index):
#        """Move the patient down until the heap property is restored."""
#        size = len(self.data)
#        while True:
#            left = 2 * index + 1
#            right = 2 * index + 2
#            smallest = index

#               smallest = left
#            if right < size and self.data[right].urgency < self.data[smallest].urgency:
#                smallest = right

#            if smallest == index:
#                break

#            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
#            index = smallest

#    def insert(self, patient):
#        """Add a new patient and restore heap order."""
#        self.data.append(patient)
#        self.heapify_up(len(self.data) - 1)

#    def peek(self):
#        """Return the most urgent patient without removing them."""
#        if not self.data:
#            return None
#        return self.data[0]

#    def remove_min(self):
#        """Remove and return the most urgent patient."""
#        if not self.data:
#            return None
#        if len(self.data) == 1:
#            return self.data.pop()

#        root = self.data[0]
#       self.data[0] = self.data.pop()
#        self.heapify_down(0)
#        return root

#    def print_heap(self):
#        print("Current Queue:")
#        if not self.data:
#            print("- (empty)")
#           return
#        for patient in self.data:
#        print(f"- {patient.name} ({patient.urgency})")



# Test your MinHeap class here including edge cases

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  # 1 is most urgent (min value)

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        """Move the patient up until the heap property is restored."""
        parent_index = (index - 1) // 2
        while index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify_down(self, index):
        """Move the patient down until the heap property is restored."""
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        """Add a new patient and restore heap order."""
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        """Return the most urgent patient without removing them."""
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        """Remove and return the most urgent patient."""
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Juan", 2))
    heap.insert(Patient("Pablo", 1))
    heap.insert(Patient("Morales", 3))
    heap.print_heap()

    print("\nNext up:", heap.peek())
    served = heap.remove_min()
    print("\nServed:", served)
    heap.print_heap()
