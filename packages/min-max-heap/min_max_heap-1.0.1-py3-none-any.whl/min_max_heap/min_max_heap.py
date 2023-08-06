from .utils import push, pop_max, pop_min, peek_max, peek_min


class MinMaxHeap():
    """An implementation of min max heap."""
    
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def push(self, item):
        return push(self.queue, item)

    def get(self):
        return pop_min(self.queue)
    
    def pop_min(self):
        return pop_min(self.queue)

    def pop_max(self):
        return pop_max(self.queue)

    def min(self):
        return peek_min(self.queue)

    def max(self):
        return peek_max(self.queue)

    def is_empty(self):
        return self.size() == 0