
import multiprocessing
import random
import time


def corrida_sapo(numero):
    distancia_maxima = 50
    tamanho_maximo_salto = random.randint(1, 5)

    distancia_percorrida = 0

    print(f"\nSapo {numero} começou a corrida!")

    while distancia_percorrida < distancia_maxima:

        salto = random.randint(0, tamanho_maximo_salto)

        distancia_percorrida += salto

        print(
            f"Sapo {numero} saltou {salto} cm. "
            f"Percorreu: {distancia_percorrida} cm."
        )

        time.sleep(0.5)

    print(
        f"\nSapo {numero} terminou! "
        f"Posição final: {distancia_percorrida} cm."
    )


def main():
    sapos = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=5) as pool:
        pool.map(corrida_sapo, sapos)

    print("\nCorrida finalizada!")


if __name__ == "__main__":
    main()
