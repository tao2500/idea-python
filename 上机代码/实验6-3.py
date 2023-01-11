class Queue:
    array = []

    def push(self, data):
        self.array.append(data)

    def pull(self):

        if len(self.array) > 0:
            data = self.array[0]
            self.array.pop(0)
            return data
        else:
            return "IndexError"


aQueue = Queue()
aQueue.push("hello")
aQueue.push(42)
print(aQueue.pull())  # hello
print(aQueue.pull())  # 42
print(aQueue.pull())  # IndexError
