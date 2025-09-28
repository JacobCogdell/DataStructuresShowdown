"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    coll_len = len(product_ids)
    set_len = len(set(product_ids))
    if coll_len == set_len:
        return False
    else:
        return True

# Duplicate type functionality is built into Python sets and so the set is a great choice for this problem.  
# If the length of the set is less than the length of the original collection, then there must be duplicates.  
# This approach allows this calculation to be solved in a simple and efficient manner from the code and the 
# computation perspective.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
from queue import Queue

class TaskQueue:
    def __init__(self):
        self.tasks = Queue()

    def add_task(self, task):
        self.tasks.put(task)

    def remove_oldest_task(self):
        return self.tasks.get() 
    
# Any time we want First In First Out (FIFO) functionality, a queue is a great choice.
# Python has several variations of queues available in the standard library.  Iselected the standard 
# queue.  The add_task maps to the standard queueu put while the remove_oldest_task maps to the queue get.
# Again, this approach allows this calculation to be solved in a simple and efficient manner from the code and the 
# computation perspective.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)

# Sets are a great choice for this problem since they automatically handle uniqueness.  
# The add method of the set will only add a value it it is not already there.  The get_unqique_count 
# maps to the len function of the set.  This code is very simpmle and efficient.  

# TESTING
print("Problem 1: Duplicate Tracker")
print(has_duplicates([10, 20, 30, 20, 40]))
print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([]))
print(has_duplicates([1, 1, 1, 1, 1]))

print("\nProblem 2: Order Manager")
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())
task_queue.add_task("Team meeting")
print(task_queue.remove_oldest_task()) 
print(task_queue.remove_oldest_task())  

print("\nProblem 3: Unique Value Counter")
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)         
tracker.add(10)
print(tracker.get_unique_count())