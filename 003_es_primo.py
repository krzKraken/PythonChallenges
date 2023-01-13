# Escriba un programa que indique si un numero es primo, luego de esto escribir los numeros primos entre el 1 y el 100
# Es primo si es divisible para si mismo y la unidad


def main():

    def esPrimo(num):
        cont = 0
        for i in range(num):
            if num % (i+1) == 0 and num > 0:
                cont += 1

        if cont == 2 or num == 1:
            return True
        else:
            return False

    numInicial = 0
    numFinal = 101
    for i in range(numInicial, numFinal):
        if esPrimo(i):
            print(i)


if __name__ == "__main__":
    main()
