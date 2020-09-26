class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.count = 0

    def append(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
            self.count += 1
        else:
            if self.count is self.capacity:
                self.count = 0
                self.stack[0] = item
                self.count += 1
            else:
                index = self.count - self.capacity
                self.stack[index] = item
                self.count += 1


    def get(self):
        return self.stack
