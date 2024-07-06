class Refueling:
    def __init__(self, p_eni, p_bey, spesa=None, litri=None):
        self.p_eni = p_eni
        self.p_bey = p_bey
        self.spesa = spesa
        self.litri = litri

    def calcola_eni_scontato(self):
        p_eni_s = self.p_eni * 0.9
        return p_eni_s

    def calcola_diff_p_bey_s_p_eni(self):
        diff_p_bey_s_p_eni = self.p_bey - self.calcola_eni_scontato()
        return diff_p_bey_s_p_eni

    def calcola_diff_p_bey_s_p_eni_perc(self):
        diff_p_bey_s_p_eni_perc = self.calcola_diff_p_bey_s_p_eni() / self.p_bey
        return diff_p_bey_s_p_eni_perc


class RefuelingCollection:
    def __init__(self):
        self.refuelings = []

    def add_refueling(self, refueling):
        self.refuelings.append(refueling)

    def calculate_average_discount(self):
        total_discount = 0
        for refueling in self.refuelings:
            total_discount += refueling.calcola_diff_p_bey_s_p_eni()
        if self.refuelings:
            return total_discount / len(self.refuelings)
        else:
            return 0

    def calculate_average_discount_percentage(self):
        total_discount_percentage = 0
        for refueling in self.refuelings:
            total_discount_percentage += refueling.calcola_diff_p_bey_s_p_eni_perc()
        if self.refuelings:
            return total_discount_percentage / len(self.refuelings)
        else:
            return 0
        
    def return_refuelings(self,index):
        refueling = self.refuelings[index]
        return refueling



# Example usage:
r1 = Refueling(1.879, 1.819)
r2 = Refueling(1.890, 1.800)
r3 = Refueling(1.870, 1.800)


collection = RefuelingCollection()
collection.add_refueling(r1)
collection.add_refueling(r2)
collection.add_refueling(r3)

average_discount = collection.calculate_average_discount()
average_discount_percentage = collection.calculate_average_discount_percentage()

print("Average discount:", average_discount)
print("Average discount percentage:", average_discount_percentage)
print()
