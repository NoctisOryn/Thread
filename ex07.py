
import multiprocessing
import random
import time


def piloto(dados):
    equipe, carro, semaforo, lock_equipe = dados

    # Impede a entrada simultânea de carros da mesma equipe
    lock_equipe.acquire()

    try:
        # Permite no máximo cinco carros na pista
        semaforo.acquire()

        try:
            print(
                f"\nEquipe {equipe} - Carro {carro} "
                f"entrou na pista!"
            )

            for volta in range(1, 4):

                tempo = random.uniform(1.5, 3.5)

                time.sleep(tempo)

                print(
                    f"Equipe {equipe} - Carro {carro} "
                    f"| Volta {volta} "
                    f"| Tempo: {tempo:.2f} segundos"
                )

            print(
                f"Equipe {equipe} - Carro {carro} "
                f"saiu da pista!"
            )

        finally:
            semaforo.release()

    finally:
        lock_equipe.release()


def main():

    equipes = 7
    carros_por_equipe = 2

    with multiprocessing.Manager() as manager:

        semaforo = manager.BoundedSemaphore(5)

        locks = [
            manager.Lock()
            for _ in range(equipes)
        ]

        tarefas = []

        for equipe in range(equipes):

            for carro in range(carros_por_equipe):

                tarefas.append((
                    equipe + 1,
                    carro + 1,
                    semaforo,
                    locks[equipe]
                ))

        with multiprocessing.Pool(processes=14) as pool:
            pool.map(piloto, tarefas)

    print("\nCorrida finalizada!")


if __name__ == "__main__":
    main()
