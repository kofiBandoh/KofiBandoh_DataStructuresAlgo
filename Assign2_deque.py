class deque:

    def __init__(self, maxSize):
        self.array = []
        self.currentSize = 0
        self.maxSize = maxSize

    def isFull(self):
        if self.currentSize >= self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def getNumberofElements(self):
        return self.currentSize
    
    def add_to_front(self, x):
        if self.currentSize == 0:
            self.array[0] = x
            return

        if not self.isFull():
            temp = []
            temp.insert(0, x)
            for i in range(self.currentSize):
                temp.insert(i + 1, self.array[i])
            self.array = temp
            self.currentSize += 1

    def add_to_back(self, x):
        self.array.insert(self.currentSize, x)
        self.currentSize += 1

    def remove_front(self):
        front = self.array[0]
        temp = []

        for i in range(self.currentSize - 1):
            temp.insert(i, self.array[i+1])
        self.array = temp
        self.currentSize -= 1
        return front

    def remove_back(self):
        back = self.array[self.currentSize-1]
        temp = []

        for i in range(self.currentSize - 1):
            temp.insert(i, self.array[i])
        self.array = temp
        self.currentSize -= 1
        return back

    def print_deque(self):
        for i in range(self.currentSize):
            print(self.array[i])

            