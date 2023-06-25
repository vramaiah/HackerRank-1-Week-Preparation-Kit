class Queue:
    """A class to represent a queue"""

    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        return self.elements.pop(0)
    
    @property
    def front(self):
        return self.elements[0]

if __name__ == "__main__":
    number_queries = int(input())
    queue = Queue()
    for i in range(number_queries):
        query = [int(part) for part in input().split()]
        type = query[0]
        if type == 1:
            queue.enqueue(item=query[1])
        elif type == 2:
            queue.dequeue()
        elif type == 3:
            print(queue.front)
