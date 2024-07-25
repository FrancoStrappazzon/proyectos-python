# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
#  - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  - Imprime el cálculo del área de un polígono de cada tipo.

class Poligono:
    def calcular_area(self):
        pass
    
class Cuadrado(Poligono):
    def __init__(self,lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado **2
    
    
class Triangulo(Poligono):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base*self.altura /2
    
class Rectangulo(Poligono):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura 
    

#Unica funcion para calcular el area de cada poligono
def calcular_area_poligono(poligono):
    area = poligono.calcular_area()
    print(f'El area del poligono es {area}')
    

cuadrado = Cuadrado(4)
triangulo = Triangulo(4,6)
rectangulo = Rectangulo(5,15)

calcular_area_poligono(cuadrado)
calcular_area_poligono(triangulo)
calcular_area_poligono(rectangulo)
