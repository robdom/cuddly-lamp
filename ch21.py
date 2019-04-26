import time
import random

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()

# stack.push(1)
# item = stack.pop()
# print(item)
# print(stack.is_empty())

# for i in range(0,6):
#     stack.push(i)

# print(stack.peek())
# print(stack.size())

# for c in "hello":
#     stack.push(c)

# reverse = ""

# for i in range(len(stack.items)):
#     reverse += stack.pop()

# print(reverse)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# a_queue = Queue()

# print(a_queue.is_empty())

# for i in range(5):
#     a_queue.enqueue(i)

# # print(a_queue.size())

# for i in range(5):
#     print(a_queue.dequeue())

# print()

# print(a_queue.size())

    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []

        for i in range(10):
            pq.enqueue("person" + str(i))

        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            # print(person)
            tix_sold.append(person)

        return tix_sold

queue = Queue()
sold = queue.simulate_line(5, 1)
# print(sold)

# Challenge 1

# for c in "yesterday":
#     stack.push(c)

# reverse = ""

# for i in range(len(stack.items)):
#     reverse += stack.pop()

# print(reverse)


# Challenge 2 - Cory's solution

list1 = [1, 2, 3, 4, 5]
list2 = []

stack = Stack()
for item in list1:
    stack.push(item)


for i in range(len(stack.items)):
    list2.append(stack.pop())

print(list2)


