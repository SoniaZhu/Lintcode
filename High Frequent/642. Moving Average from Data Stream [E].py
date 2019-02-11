from queue import Queue

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.queue = Queue()
        self.sum = 0   #0.0

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        if self.queue.qsize() >= self.size:
            self.sum -= self.queue.get()
        self.sum += val
        self.queue.put(val)
        return self.sum / self.queue.qsize()

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.sum = [0] * (size + 1)
        self.index = 0
        self.size = size

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        self.index += 1
        self.sum[self.mod(self.index)] = self.sum[self.mod(self.index - 1)] + val
        if self.index >= self.size:
            return (self.sum[self.mod(self.index)] - self.sum[self.mod(self.index - self.size)]) / self.size
        else:
            return (self.sum[self.mod(self.index)]) / self.index

    def mod(self, num):
        return num % (self.size + 1)
