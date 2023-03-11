# * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.


def main():
    def esAnagrama(word1: str, word2: str):

        if sorted(word1.lower()) == sorted(word2.lower()):
            return "Es Anagrama"
        else:
            return "No es Anagrama"

    print(esAnagrama("caso", "Cosa"))


if __name__ == "__main__":
    main()
