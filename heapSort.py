class MaxHeap:
    def __init__(self, arr):
        # Initialize the heap with an array and build the max-heap
        self.heap = arr
        self.build_max_heap()

    def build_max_heap(self):
        # Build the max-heap by applying max-heapify from the last non-leaf node
        for i in range(len(self.heap)//2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        # Ensure the heap property is maintained at the given index
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index
        largest = i  # Assume the current node is the largest

        # Compare the left child with the current largest
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        # Compare the right child with the current largest
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        # If the largest is not the current node, swap and continue heapifying
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def extract_max(self):
        # Remove and return the maximum element (root of the heap)
        if len(self.heap) < 1:
            return None  # Return None if heap is empty
        max_item = self.heap[0]  # The root holds the max value
        self.heap[0] = self.heap[-1]  # Replace the root with the last element
        self.heap.pop()  # Remove the last element
        self.max_heapify(0)  # Restore the max-heap property
        return max_item

    def insert(self, key):
        # Insert a new element into the heap and maintain the heap property
        self.heap.append(key)  # Add the new element to the end of the heap
        i = len(self.heap) - 1  # Start from the last index
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            # Swap with the parent if the current element is greater
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2  # Move up to the parent

    def get_max(self):
        # Return the maximum element (root of the heap)
        return self.heap[0] if self.heap else None

def heapsort(arr):
    # Function to perform Heapsort using the MaxHeap class
    heap = MaxHeap(arr)  # Create a MaxHeap instance
    sorted_arr = []
    while len(heap.heap) > 0:
        # Extract the maximum element and add it to the sorted array
        sorted_arr.append(heap.extract_max())
    return sorted_arr[::-1]  # Reverse to get ascending order (since we extract max)

# Example usage:
arr = [4, 10, 3, 5, 1]
sorted_arr = heapsort(arr)  # Perform Heapsort
print("Sorted Array:", sorted_arr)  # Output the sorted array
