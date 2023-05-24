import threading

def contador_crescente():
    for i in range(1, 501):
    print(i)

def contador_decrescente():
    for i in range(500, 0, -1):
    print(i)

thread_crescente = threading.Thread(target=contador_crescente)
thread_decrescente = threading.Thread(target=contador_decrescente)

thread_crescente.start()
thread_decrescente.start()

thread_crescente.join()
thread_decrescente.join()