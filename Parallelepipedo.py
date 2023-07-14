""" class Prallelepipedo:

    def __init__(self, larghezza, profondita, altezza):
        self._larghezza = larghezza
        self._profonndita = profondita
        self._altezza = altezza
 """


class Parallelepipedo_retto:
    NUMERO_SPIGOLI = 12
    NUMERO_VERTICI = 8

    def __init__(self, larghezza: float, profondita: float, altezza: float):
        self._larghezza = larghezza
        self._profondita = profondita
        self._altezza = altezza
   
    # get e set
        # larghezza    
    def get_larghezza(self) -> float:
        return self._larghezza
    
    def set_larghezza(self, larghezza: float) -> None:
        if larghezza > 0:
            self._larghezza = larghezza
        else:
            print("Son ammessi solo valori > 0!!")
    
        # profondita
    def get_profondita(self) -> float:
        return self.get_profondita

    def set_profondita (self, profondita: float) -> None:
        if profondita > 0:
            self._profondita = profondita
        else:
            print("Son ammessi solo valori > 0!!")   

        # altezza
    def get_altezza(self) -> float:
        return self.get_altezza

    def set_altezza (self, altezza: float) -> None:
        if altezza > 0:
            self._altezza = altezza
        else:
            print("Son ammessi solo valori > 0!!")   

    # volume
    def calcola_volume(self) -> float:
        volume = self._larghezza * self._profondita * self._altezza
        return volume

    # superfici
    def area_base(self) -> float:
        area = self._larghezza * self._profondita
        return area
    
    def area_laterale(self) -> float:
        area = (self._larghezza*2 + self._profondita*2) * self._altezza
        return area
    
    def area_totale(self) -> float:
        area = self.area_base*2 + self.area_laterale
        return area 

    # metodo __str__
    def __str__(self) -> str:
        return f"Parallelepipedo_retto(lar={self._larghezza}, pro={self._profondita}, alt={self._altezza})"