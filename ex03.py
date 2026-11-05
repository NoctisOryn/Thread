import threading
import time
import random

distancia_max = 30  # cm
pulo_max = 5        # cm

def sapo(id):
    global distancia_max
    global pulo_max
    percorrido = 0
    while percorrido < distancia_max:
        pulo = random.randint(1, pulo_max)
        percorrido += pulo
        if percorrido > distancia_max:
            percorrido = distancia_max
        print(f"Sapo {id} pulou {pulo} cm e já percorreu {percorrido} cm")
        time.sleep(random.uniform(0.2, 0.5))
    print(f"*** Sapo {id} CHEGOU! ***")

def main():
    threads = [threading.Thread(target=sapo, args=(i,)) for i in range(1, 6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()