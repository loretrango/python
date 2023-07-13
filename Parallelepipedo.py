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

""" par1 = Parallelepipedo(int(input("larghezza: ")), int(input("Profondità: ")), int(input("Altezza: ")))

par2 = Parallelepipedo(int(input("larghezza: ")), int(input("Profondità: ")), int(input("Altezza: ")))

volume = par1.calcola_volume()
print(volume)

area = par1.area_laterale()
print(area)

par1.chi_sei()

rapporto_larghezze = par1.lar / par2.lar
print(rapporto_larghezze)  """