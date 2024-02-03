## Classe Rettangolo
class Rettangolo:
    ## costruttore dell'oggetto
    def __init__(self, a = None, b = None, area = None):
        self.a = a
        self.b = b
        self.area = area

    ## Metodi get
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def get_perimetro(self):
        perimetro = self.a * 2 + self.b * 2
        return perimetro
    
    def get_area(self):
        area = self.a * self.b
        return area


    # Stampa le misure
    def print_misure(self):
        print("Misure rettangolo:\na = ",self.a,"\nb = ",self.b)

    # Stampa area
    def print_area(self):
        self.area = self.a * self.b
        print("Area = ",self.a*self.b)
        return self.area
    
    ## Metodo confronta aree rettangoli
    def confronta_area(self, altro_rettangolo):
        area_self = self.get_area()
        area_altro = altro_rettangolo.get_area()

        if area_self > area_altro:
            return f"L'area del primo rettangolo è maggiore del secondo"
        elif area_self < area_altro:
            return f"Larea del secondo rettangolo è maggiore del primo"
        else:
            return f"Le aree dei rettangoli sono uguali"
 

# Crea l'oggetto r1 
r1 = Rettangolo(2,4)
print("Area: ",r1.get_area())
print("Perimetro: ", r1.get_perimetro())

# Crea l'oggetto r2
r2 = Rettangolo(33,55)
print("Area: ",r2.get_area())
print("Perimetro: ", r2.get_perimetro())

# confronta le aree
print(r1.confronta_area(r2))
