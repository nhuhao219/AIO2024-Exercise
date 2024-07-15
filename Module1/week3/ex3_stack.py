class MyStack:
    def __init__(self, capacity):
        self.__cap = capacity
        self.__data = []

    def __call__(self):
        print(f"Capacity={self.__cap}, length={
              len(self.__data)}, data={self.__data}")

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

    def push(self, value):
        if self.is_full():
            print("Stack is full!")
        else:
            return self.__data.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.__data.pop()

    def top(self):
        return self.__data[-1]


m = MyStack(4)
m.push(3)
m.push(4)
m.push(5)
m.push(6)
m.push(7)
m()
m.pop()
print(m.top())
