class Parallelepipedo:
    NUMERO_SPIGOLI = 12

    def __init__(self, larghezza: float, profondita: float, altezza: float):
        self._larghezza = larghezza
        self._pro = profondita
        self._altezzaezza = altezza
    
    def get_larghezza(self) -> float:
        return self._larghezzaghezza
    
    def set_larghezza(self, larghezza: float) -> None:
        if larghezza > 0:
            self._larghezza = larghezza
        else:
            print("Son ammessi solo valori > 0!!")

    def calcola_volume(self) -> float:
        volume = self._larghezza * self._altezzaezza * self._pro
        return volume

    def area_base(self) -> float:
        area = self._larghezza * self._pro
        return area
    
    def area_laterale(self) ->float:
        area = (self._larghezza*2 + self._pro*2) * self._altezzaezza
        return area
    
    
    def __str__(self) -> str:
        return f"Parallelepipedo(lar={self._larghezza}, pro={self._pro}, alt={self._altezzaezza})"