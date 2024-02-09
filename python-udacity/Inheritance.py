
# ? Clase padre Clothing
"""
more info https://www.w3schools.com/python/python_inheritance.asp

"""
class Clothing:
    """
    Clase Ropa, tiene los atributos comumes para las clases hijas o heredeadas
    """
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
        
    def change_price(self, price):
        self.price = price
    
    def calculate_discount(self, discount):
        return self.price * (1 - discount)
    

#? Clase hija o herencia Shirt
class Shirt(Clothing):
    """
    Clase Camiseta, tiene los atributos heredados de la clases clothing #! se puede agregar mas atributos en la construccion de la clase
    """
    def __init__(self, color, size, style, price, long_or_short):
        #? Esto es un constructor de la clase padre 
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short
    
    def double_price(self):
        self.price = 2*self.price
        
class Pants(Clothing):
    """Clase Pantalon, tiene los atributos heredados de la clases clothing  #! Se peuden sobreescribir los metodos de la clase padre"""
    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist
    #? Sobre escribe el metodo de descuentos
    def calculate_discount(self, discount):
       return self.price * (1 - discount / 2)