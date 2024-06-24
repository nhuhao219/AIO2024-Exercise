class MyQueue:
    def __init__(self, capacity):
        self.__cap = capacity
        self.__data = []

    def __call__(self):
        print(f"Capacity = {self.__cap}, length = {
              len(self.__data)}, data = {self.__data}")

    def is_full(self):
        if len(self.__data) == self.__cap:
            return True
        else:
            return False

    def is_empty(self):
        if len(self.__data) == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            print("Stack is full!")
        else:
            return self.__data.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.__data.pop(0)

    def front(self):
        return self.__data[0]


m = MyQueue(4)
m.enqueue(3)
m.enqueue(4)
m.enqueue(5)
m.enqueue(6)
m.enqueue(7)
m()
m.dequeue()
print(m.front())
