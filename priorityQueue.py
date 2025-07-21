class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        # Initialize a Task object with task details
        self.task_id = task_id  # Task identifier
        self.priority = priority  # Task priority (higher value means higher priority)
        self.arrival_time = arrival_time  # When the task arrived
        self.deadline = deadline  # Deadline for the task

    def __lt__(self, other):
        # Define comparison for tasks based on priority (max-heap: higher priority first)
        return self.priority > other.priority  # Tasks with higher priority should come first

class PriorityQueue:
    def __init__(self):
        # Initialize an empty priority queue represented as a heap
        self.heap = []

    def insert(self, task):
        # Insert a new task into the priority queue
        self.heap.append(task)  # Add the task at the end of the heap
        i = len(self.heap) - 1  # Start from the last index
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            # If the task has a higher priority than its parent, swap them
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2  # Move up to the parent

    def extract_max(self):
        # Remove and return the task with the highest priority
        if len(self.heap) < 1:
            return None  # Return None if the heap is empty
        max_task = self.heap[0]  # The root holds the highest priority task
        self.heap[0] = self.heap[-1]  # Replace root with the last task
        self.heap.pop()  # Remove the last task
        self.max_heapify(0)  # Restore the max-heap property
        return max_task

    def max_heapify(self, i):
        # Restore the heap property after removal (heapify down)
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index
        largest = i  # Assume current node is the largest
        
        # Compare with the left child
        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left
        # Compare with the right child
        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right
        # If the largest is not the current node, swap and continue heapifying
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def increase_key(self, task, new_priority):
        # Increase the priority of an existing task
        task.priority = new_priority  # Update the priority
        i = self.heap.index(task)  # Find the task's index in the heap
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            # If the task has higher priority than its parent, swap them
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2  # Move up to the parent

# Example usage:
pq = PriorityQueue()

# Insert tasks with task_id, priority, arrival_time, and deadline
pq.insert(Task(1, 3, "2025-01-01", "2025-01-02"))
pq.insert(Task(2, 5, "2025-01-01", "2025-01-02"))
pq.insert(Task(3, 2, "2025-01-01", "2025-01-02"))

# Extract max (highest priority task)
max_task = pq.extract_max()
print("Task with highest priority:", max_task.task_id)

# Modify task priority
task_to_increase = pq.heap[0]
pq.increase_key(task_to_increase, 7)
print("Task after priority increase:", task_to_increase.priority)
