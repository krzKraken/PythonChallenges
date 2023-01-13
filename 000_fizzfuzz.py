# /*
#  * Reto #0
#  * EL FAMOSO "FIZZ BUZZ"
#  * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

for num in range(1, 101):
    divisibleByTre = num % 3 == 0
    divisibleByFive = num % 5 == 0

    if divisibleByTre and divisibleByFive:
        print("FIZZBUZZ")
    elif divisibleByTre:
        print("FIZZ")
    elif divisibleByFive:
        print("BUZZ")
    else:
        print(num)
