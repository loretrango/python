import tkinter as tk

def calculate_parallelepipedo():
    larghezza = float(entry_larghezza.get())
    profondita = float(entry_profondita.get())
    altezza = float(entry_altezza.get())

    perimetro_base = 2 * larghezza + 2 * profondita
    result_perimetro_base.config(text=f"Perimetro di base: {perimetro_base}")

    prof_per_alt = profondita * altezza
    result_prof_per_alt.config(text=f"Profondità per altezza: {prof_per_alt}")

    larg_per_alt = larghezza * altezza
    result_larg_per_alt.config(text=f"Larghezza per altezza: {larg_per_alt}")

    area_base = larghezza * profondita
    result_area_base.config(text=f"Area di base: {area_base}")

    area_laterale = perimetro_base * altezza
    result_area_laterale.config(text=f"Area laterale: {area_laterale}")

    area_totale = area_base + area_laterale
    result_area_totale.config(text=f"Area totale: {area_totale}")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Calcola Parallelepipedo")

# Create labels
label_larghezza = tk.Label(window, text="Larghezza:")
label_larghezza.pack()

label_profondita = tk.Label(window, text="Profondità:")
label_profondita.pack()

label_altezza = tk.Label(window, text="Altezza:")
label_altezza.pack()

# Create entry fields
entry_larghezza = tk.Entry(window)
entry_larghezza.pack()

entry_profondita = tk.Entry(window)
entry_profondita.pack()

entry_altezza = tk.Entry(window)
entry_altezza.pack()

# Create a button
button_calculate = tk.Button(window, text="Calculate", command=calculate_parallelepipedo)
button_calculate.pack()

# Create result labels
result_perimetro_base = tk.Label(window, text="Perimetro di base: ")
result_perimetro_base.pack()

result_prof_per_alt = tk.Label(window, text="Profondità per altezza: ")
result_prof_per_alt.pack()

result_larg_per_alt = tk.Label(window, text="Larghezza per altezza: ")
result_larg_per_alt.pack()

result_area_base = tk.Label(window, text="Area di base: ")
result_area_base.pack()

result_area_laterale = tk.Label(window, text="Area laterale: ")
result_area_laterale.pack()

result_area_totale = tk.Label(window, text="Area totale: ")
result_area_totale.pack()

# Run the GUI main loop
window.mainloop()
