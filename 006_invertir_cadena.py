"""
 Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH" 
"""


def main():
    cadena = "hola mundo"
    newCadena = ""

    for i, char in enumerate(cadena):
        if i < len(cadena):
            newCadena = newCadena + cadena[len(cadena)-i-1]
    print(newCadena)


if __name__ == "__main__":
    main()
