"""
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.

"""


class Poligono:
    def area(self):
        # Se reescribe en cada Poligono
        pass

    def printArea(self):
        # Se reescribe en cada Poligono
        pass


class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

    def printArea(self):
        print(f"El area del triangulo es: {self.area()}")


class Rectangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def printArea(self):
        print(f"El area del Rectangulo es: {self.area()}")


class Cuadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def printArea(self):
        print(f"El area del Cuadrado es: {self.area()}")


def main():
    triangulo = Triangulo(2, 6).printArea()
    rectangulo = Rectangulo(2, 10).printArea()
    cuadrado = Cuadrado(2).printArea()


if __name__ == "__main__":
    main()
