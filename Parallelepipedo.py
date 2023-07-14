class Prisma:
    def __init__(self, area_base: float, altezza: float = None, volume = None):
        self._area_base = area_base
        self._altezza = altezza
        self._volume = volume
        if self._volume == None and self._area_base !=None and self._altezza != None:
            self._volume = self._area_base * self._altezza
    
    def calcola_volume() -> float:
        volume = self._area_base * self.altezza
        return volume

class Parallelepipedo(Prisma):
    def __init__(self, larghezza: float, profondita: float, altezza: float, area_base: float = None):
        self._larghezza = larghezza
        self._profondita = profondita
        self._altezza = altezza
        self._area_base = area_base
        if self._area_base == "":
            self._area_base = self.area_base()
 
     # volume
    def calcola_volume(self) -> float:
        volume = self._larghezza * self._profondita * self._altezza
        return volume

    # superfici
    def area_base(self) -> float:
        area = self._larghezza * self._profondita
        return area

class ParallelepipedoRetto(Parallelepipedo):
    def __init__(self, larghezza: float, profondita: float, altezza: float):
        self._larghezza = larghezza
        self._profondita = profondita
        self._altezza = altezza
   
    # get e set
        # larghezza    
    def larghezza(self) -> float:
        return self._larghezza
    
    def larghezza(self, larghezza: float) -> None:
        if larghezza > 0:
            self._larghezza = larghezza
        else:
            print("Son ammessi solo valori > 0!!")
    
        # profondita
    def profondita(self) -> float:
        return self.get_profondita

    def profondita (self, profondita: float) -> None:
        if profondita > 0:
            self._profondita = profondita
        else:
            print("Son ammessi solo valori > 0!!")   

        # altezza
    def altezza(self) -> float:
        return self.get_altezza

    def altezza (self, altezza: float) -> None:
        if altezza > 0:
            self._altezza = altezza
        else:
            print("Son ammessi solo valori > 0!!")   

    # # volume
    # def calcola_volume(self) -> float:
    #     volume = self._larghezza * self._profondita * self._altezza
    #     return volume

    #superfici
    
    # def area_base(self) -> float:
    #     area = self._larghezza * self._profondita
    #     return area
    
    def area_laterale(self) -> float:
        area = (self._larghezza*2 + self._profondita*2) * self._altezza
        return area
    
    def area_totale(self) -> float:
        area = self.area_base()*2 + self.area_laterale()
        return area 

    # metodo __str__
    def __str__(self) -> str:
        return f"Parallelepipedo_retto(lar={self._larghezza}, pro={self._profondita}, alt={self._altezza})"
    

par1 = ParallelepipedoRetto(2,4,5)
print(par1.__str__())
print("Volume", par1.calcola_volume())
print("Area di base", par1.area_base())

print("par_nonRetto")
par_nonRetto = Parallelepipedo(2,4,5,"")
print(par_nonRetto._altezza)
print("Volume", par_nonRetto.calcola_volume())
print("Area_base", par_nonRetto._area_base)
print("Area base", par_nonRetto.area_base())
print("Area_base", par_nonRetto._area_base)

print("Prisma")
prisma = Prisma(altezza=2, area_base=10)
print(prisma._volume)