"""
More info: 
- Python's Instance, Class, and Static Methods Demystified:  https://realpython.com/instance-class-and-static-methods-demystified/
- Class Vs Instance Attributes: https://python-course.eu/oop/class-instance-attributes.php
- Mixins for fun and profit: https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556
- Primer on Python Decorators: https://realpython.com/primer-on-python-decorators/
"""


from rich import print

class Persona:
    def __init__(self, name, age, experiencia):
        self.name = name
        self.age = age
        self.experiencia = experiencia
    
    def hablar(self):
        return "Hola me llamo {} y tengo {} anios".format(self.name, self.age)
    
    def __add__(self, other):
        return self.experiencia + other.experiencia
    

    
class Programmer(Persona):
    def __init__(self, name, age,  experiencia, skills ):
        Persona.__init__(self, name, age, experiencia)
        self.skills = skills
    
    def hablar(self):
        return "Hola me llamo {} y tengo {} anios y tengo habilidades {} con {} anos de experiencia ".format(self.name, self.age, self.skills, self.experiencia)
    
    def __str__(self):
        return self.hablar()

def main():
    print("[bold green] Magic Method [/bold green]")
    programador_1 = Programmer("Cristian", 25, 5,"python")
    programador_2 = Programmer("Jaime", 33, 20, "java")	
    print("______________ Magic Method _____________")
    print(programador_1)
    print(programador_2)
    print("_____________ Magic Add _________________")
    
    print("Persona 1 + Persona 2 = {} anos de experiencia".format(programador_1 + programador_2))
    
    
if __name__ == "__main__":
    main()