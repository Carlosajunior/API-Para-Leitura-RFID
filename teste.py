from threading import *
import time
globalIsOver = False
semaforo = Semaphore(1)
def printar():
    semaforo.acquire()
    i = 1
    print(i)
    i += 1 
    time.sleep(1)
    semaforo.release()
Printar = Thread(target= printar, args = ())
def lerTAG(timeout):
    timer(timeout)
    
    x = 0
    while not over():
        if not Printar.is_alive():
            Printar.start()
    print('Exited run function.')

def timer(time):
    t = Timer(time, setOver)
    t.start()

def setOver():
    global globalIsOver
    globalIsOver = True

def over():
    global globalIsOver
    return globalIsOver



lerTAG(timeout=10)