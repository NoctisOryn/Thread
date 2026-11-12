
import multiprocessing
import time
import random


def controlar_carro(dados):
    sentido, lock = dados

    with lock:
        print(f"Carro entrando pelo sentido: {sentido}")

        time.sleep(random.uniform(1, 3))

        print(f"Carro saiu pelo sentido: {sentido}")


def main():
    sentidos = ["Norte", "Sul", "Leste", "Oeste"]

    with multiprocessing.Manager() as manager:
        lock = manager.Lock()

        tarefas = [(sentido, lock) for sentido in sentidos]

        with multiprocessing.Pool(processes=4) as pool:
            pool.map(controlar_carro, tarefas)

    print("Cruzamento liberado!")


if __name__ == "__main__":
    main()