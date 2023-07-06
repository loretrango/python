import tkinter as tk
import math

def calculate_cono():
    global raggio, altezza, apotema

    occorrenze = ['raggio' in locals(), 'altezza' in locals(), 'apotema' in locals()]
    numero_occorrenze_vere = occorrenze.count(True)

    while numero_occorrenze_vere < 2:
        cosa_conosci = ""
        if not 'raggio' in locals():
            if entry_raggio.get():
                cosa_conosci = "r"
                raggio = float(entry_raggio.get())
        if not 'altezza' in locals():
            if entry_altezza.get():
                cosa_conosci = "h"
                altezza = float(entry_altezza.get())
        if not 'apotema' in locals():
            if entry_apotema.get():
                cosa_conosci = "a"
                apotema = float(entry_apotema.get())

        occorrenze = ['raggio' in locals(), 'altezza' in locals(), 'apotema' in locals()]
        numero_occorrenze_vere = occorrenze.count(True)

    # Perform calculations and display results

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Calcola Cono")

# Create labels
label_raggio = tk.Label(window, text="Raggio:")
label_raggio.pack()

label_altezza = tk.Label(window, text="Altezza:")
label_altezza.pack()

label_apotema = tk.Label(window, text="Apotema:")
label_apotema.pack()

# Create entry fields
entry_raggio = tk.Entry(window)
entry_raggio.pack()

entry_altezza = tk.Entry(window)
entry_altezza.pack()

entry_apotema = tk.Entry(window)
entry_apotema.pack()

# Create a button
button_calculate = tk.Button(window, text="Calculate", command=calculate_cono)
button_calculate.pack()

# Create result labels
# You can add labels for displaying the calculated results here

# Run the GUI main loop
window.mainloop()
