class Parallelepipedo:
    def __init__(self, larghezza, profondita, altezza):
        self.lar = larghezza
        self.pro = profondita
        self.alt = altezza
    
    def calcola_volume(self):
        volume = self.lar * self.alt * self.pro
        print(volume)
        return volume

    def area_base(self):
        area = self.lar * self.pro
        print(area)
        return area
    
    def area_laterale(self):
        area = (self.lar*2 + self.pro*2) * self.alt
        print(area)
        return area
    
    def chi_sei(self):
        print(f"Sono un parallelepipedo di {self.lar}x{self.pro}x{self.alt}")