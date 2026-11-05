import threading
import time
import random

def soma_linha(parametros):
    id = parametros[0]
    valores = parametros[1]
    soma = 0
    for v in valores:
        soma += v
        time.sleep(0.2)
    print("Linha", id, "-> valores:", valores, "| soma:", soma)

def main():
    threads = []
    for chamada in range(3):
        id = chamada + 1
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        v3 = random.randint(1, 100)
        v4 = random.randint(1, 100)
        v5 = random.randint(1, 100)
        parametros = [id, [v1, v2, v3, v4, v5]]
        t = threading.Thread(target=soma_linha, args=(parametros,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()