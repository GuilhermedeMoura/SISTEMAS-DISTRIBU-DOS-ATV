import threading

vector = [i for i in range(1, 1001)]
scalar = 2

class Multiply(threading.Thread):
def init(self, start, end):
threading.Thread.init(self)
self.start = start
self.end = end

def run(self):
    for i in range(self.start, self.end):
        vector[i] *= scalar

threads = []

for i in range(0, 1000, 100):
thread = Multiply(i, i+100)
threads.append(thread)
thread.start()

for thread in threads:
thread.join()

print(vector)