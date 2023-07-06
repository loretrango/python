import tkinter as tk
import sys
import datetime
import math
import inspect

# window = tk.Tk()
# window.title("Finestra di prova")


# label_larghezza = tk.Label(window, text="Testo label                ")
# label_larghezza.pack()

# window.mainloop()

# #####  iuhuì
# print()
def ripeti_frase():
    with open("output.txt", "w") as file:
        frase = input("Cosa vuoi scrivere? ")
        righe = int(input("Su quante righe lo vuoi scrivere? "))
        colonne = int(input("Su quante colonne lo vuoi scrivere? "))
        riga=0
        colonna=0 
        input("Premi un tasto per iniziore: ...")
        for riga in range(righe):
            for colonna in range(colonne):
                file.write(frase+". ")
                print(frase+". ", end="")
            file.write("\n")
            print("\n")

ripeti_frase()

