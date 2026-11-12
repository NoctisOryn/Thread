
import multiprocessing
import time
import random


def pessoa(numero_lock):
    numero, lock = numero_lock

    velocidade = random.uniform(4, 6)
    tempo_porta = random.uniform(1, 2)

    distancia = 200
    tempo_caminhada = distancia / velocidade

    print(
        f"Pessoa {numero}: iniciou caminhada. "
        f"Velocidade: {velocidade:.2f} m/s"
    )

    time.sleep(tempo_caminhada)

    print(f"Pessoa {numero}: chegou à porta.")

    with lock:
        print(f"Pessoa {numero}: abriu a porta.")

        time.sleep(tempo_porta)

        print(f"Pessoa {numero}: atravessou a porta.")


def main():
    with multiprocessing.Manager() as manager:
        lock = manager.Lock()

        tarefas = [
            (numero, lock)
            for numero in range(1, 5)
        ]

        with multiprocessing.Pool(processes=4) as pool:
            pool.map(pessoa, tarefas)

    print("Todas as pessoas atravessaram!")


if __name__ == "__main__":
    main()
