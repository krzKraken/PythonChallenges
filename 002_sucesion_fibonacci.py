# * Dificultad: DIFÍCIL
# *
# * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# * 0, 1, 1, 2, 3, 5, 8, 13...


def main():
    fibonnaci = []
    for i in range(0, 10):
        if i == 0:
            fibonnaci.append(0)
        if i == 1:
            fibonnaci.append(1)
        if i > 1:
            val = fibonnaci[i - 1] + fibonnaci[i - 2]
            fibonnaci.append(val)

    print(fibonnaci)


if __name__ == "__main__":
    main()
