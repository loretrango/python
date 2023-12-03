import math
import turtle

base = float(input("Base: "))
altezza = float(input("Altezza: "))

def rettangolo(base,altezza):

    area = base * altezza / 2
    perimetro = (base + altezza) * 2
    semiperimetro = perimetro / 2

    diagonale_con_radice = math.pow(base**2 + altezza**2, 1/2)
    diagonale_con_potenza = (base**2 + altezza**2)**(1/2)
    diagonale_con_radice = round(diagonale_con_potenza, 2)
    diagonale_con_potenza = round(diagonale_con_potenza, 2)

    print()
    print("DATI:")
    print("Base: ", base)
    print("Altezza: ", altezza)

    print()
    print("SVOLGIMENTO:")
    print("Area = base * altezza / 2 = ", f"{base}*{altezza}/2 = ", area)
    print("Perimetro = (base+altezza)*2 = ",f"({base}+{altezza})*2 = ", perimetro)
    print("Semiperimetro = perimetro/2 = ", semiperimetro)
    print("Diagonale (formula radice) = (base**2 + altezza**2)**(1/2) = ", diagonale_con_radice)
    print("Diagonale (formula potenza) = (base**2 + altezza**2)**(1/2) = ", diagonale_con_potenza)

rettangolo(base,altezza)



