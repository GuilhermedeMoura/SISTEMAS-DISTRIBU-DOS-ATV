import threading

matrix = [[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]]

class RowSum(threading.Thread):
def init(self, row):
threading.Thread.init(self)
self.row = row

def run(self):
    row_sum = sum(self.row)
    print(f"Sum of row {matrix.index(self.row) + 1}: {row_sum}")
    
threads = []

for row in matrix:
thread = RowSum(row)
threads.append(thread)
thread.start()

for thread in threads:
thread.join()