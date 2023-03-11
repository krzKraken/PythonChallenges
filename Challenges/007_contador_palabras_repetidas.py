"""
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""
import re


def main():
    coincidencias = {'hola': 0, 'mi': 0}

    def contadorPalabras(frase):
        frase = frase.lower()
        palabras = re.sub(r'[^a-z0-9\s]', '', frase).split(' ')
        print(palabras)

        for palabra in palabras:
            try:
                coincidencias[str(palabra)] += 1
            except:
                if palabra != '':
                    coincidencias[str(palabra)] = 1
        print(coincidencias)

    contadorPalabras(
        "hola, mi nombre es el kraken, el demente   kraken")


if __name__ == "__main__":
    main()
