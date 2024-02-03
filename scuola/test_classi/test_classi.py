## Classe Rettangolo
class Rettangolo:
    ## costruttore dell'oggetto
    def __init__(self, a = None, b = None, area = None):
#        self.a = a
#        self.b = b
#        self.area = area
        if area is not None and a is not None:
            self.b = area / a
            self.a = a
            
        elif area is not None and b is not None:
            self.a = area / b
            self.b = b
            
        elif a is not None and b is not None:
            self.a = a
            self.b = b
        
        elif a is None and b is None:
            self.a = None
            self.b = None
    
    ## repr method
    def __repr__(self):
        if self.a is not None and self.b is not None and self.area is not None:
            return f"Rettangolo({self.a},{self.b},{self.area}"
        elif self.a is not None and self.b is not None and self.area is None:
            return f"Rettangolo({self.a},{self.b},None"
        elif self.a is not None and self.area is not None:
            return f"Rettangolo({self.a},None,{self.area}"
        elif self.b is not None and self.area is not None:
            return f"Rettangolo(None,{self.b},{self.area}"

    ## Metodi get
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def get_perimetro(self):
        perimetro = self.a * 2 + self.b * 2
        return perimetro
    
    def get_area(self):
        if (self.a is None and self.b is None) or (self.a is None and self.area is None) or (self.b is None and self.area is None):
            #raise ValueError("Non è possibile calcolare l'area")
            print("impossibile calcolare l'area")
            

        elif self.a is not None and self.b is not None:
            area = self.a * self.b
        else:
            area = self.area

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
        rapporto_aree = area_self/area_altro
        print("Rapporto area primo rett/secondo rett:",rapporto_aree)

        if area_self > area_altro:
            return f"L'area del primo rettangolo è maggiore del secondo"
        elif area_self < area_altro:
            return f"Larea del secondo rettangolo è maggiore del primo"
        else:
            return f"Le aree dei rettangoli sono uguali"
        
class Parallelogramma:
    def __init__(self, a = None, b = None, ha = None, hb = None, area = None):
        self.a = a
        self.b = b
        self.ha = ha
        self.hb = hb
        self.area = area

    def calcola_area(self):
        if self.a is not None and self.ha is not None:
            area = self.a * self.ha
            return area
        elif self.b is not None and self.hb is not None:
            area = self.b * self.hb
            return area

    def calcola_ha(self):
        if self.area is not None and self.a is not None:
            ha = self.area / self.a
            return ha
    
    def calcola_hb(self):
        if self.area is not None and self.b is not None:
            hb = self.area / self.b
            return hb

    def calcola_a(self):
        if self.area is not None and self.ha is not None:
            a = self.area / self.ha
            return a
    
    def calcola_b(self):
        if self.area is not None and self.hb is not None:
            b = self.area / self.hb
            return b
        
    def set_area(self, area):
        self.area = area

 
class Trapezio:
    def __init__(self) -> None:
        pass

class Quadrato:
    def __init__(self) -> None:
        pass

class Rombo:
    def __init__(self) -> None:
        pass


### RETTANGOLI
print("Esempio di programmazione orientata agli oggetti, varie istanze di rettangoli")
# Crea l'oggetto r1 
print("r1")
r1 = Rettangolo(2,4)
print("Rettangolo(2,4)")
print("a = ",r1.a)
print("b = ",r1.b)
print("Area: ",r1.get_area())
print("Perimetro: ", r1.get_perimetro())
print()


# Crea l'oggetto r2
print("r2")
r2 = Rettangolo(33,55)
print("Rettangolo(33,55)")
print("a = ",r2.a)
print("b = ",r2.b)
print("Area: ",r2.get_area())
print("Perimetro: ", r2.get_perimetro())
print()

# Crea l'oggetto r3, solo alcuni parametri
print("r3")
r3_str = "Rettangolo(None,4,8)"
r3 = eval(r3_str)
#print("Rpresentation of the object: ", repr(r3))
print(r3_str)
print("a = ",r3.a)
print("b = ",r3.b)
print("Area: ",r2.get_area())
print("Perimetro: ", r2.get_perimetro())
print()

# Crea l'oggetto r4, tutti i parametri mancanti
print("r4")
r4 = Rettangolo(4,None,40)
print("Rettangolo(4,None,40)")
print("a = ",r4.a)
print("b = ",r4.b)
print("Area: ",r4.get_area())
print()

# confronta le aree
confronto1_str = "r1.confronta_area(r2)"
print(confronto1_str)
print(eval(confronto1_str))

print()
### PARALLELOGRAMMI
print("PARALLELOGRAMMI")

p1 = Parallelogramma(ha=2,area=10)
print("p1")
print("a: ",p1.a)
print("b: ",p1.b)
print("ha: ",p1.ha)
print("hb: ",p1.hb)
print("Area: ", p1.area)
print(p1.area)
print(p1.area)
ha = p1.calcola_ha()
print("Calcola ha: ", ha)
print("Calcola a: ", p1.calcola_a())

