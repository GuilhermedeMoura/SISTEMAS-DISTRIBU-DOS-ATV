import threading

vector = list(range(1, 101)) 
total_sum = 0 

def sum_vector_part(start, end):
global total_sum
part_sum = sum(vector[start:end]) 
print(f"Soma da parte do vetor de {start+1} a {end}: {part_sum}") 
total_sum += part_sum 

thread1 = threading.Thread(target=sum_vector_part, args=(0, 25))
thread2 = threading.Thread(target=sum_vector_part, args=(25, 50))
thread3 = threading.Thread(target=sum_vector_part, args=(50, 75))
thread4 = threading.Thread(target=sum_vector_part, args=(75, 100))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(f"Soma total do vetor: {total_sum}") 