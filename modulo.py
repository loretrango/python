import math
import sys
import datetime
import pdfkit
import random
import tkinter as tk
import time

import matplotlib.pyplot as plt
import numpy as np
import psutil #PC temperature

from Solidi import ParallelepipedoRetto



#from tee import Tee
#import numbers
#import inspect

#### MENU
def menu():
    def menu_elenco():
        print("MENU:")
        print("1 - Calcola cilindro")
        print("2 - Calcola cono")
        print("3 - Calcola parallelepipedo")
        print("4 - Calcola Pitagora")
        print("5 - Serie di Fibonacci")
        print("6 - Insiemi")
        print("7 - Validità triangolo")
        print("8 - Calcola trapezio")
        print("9 - Quadrato")
        print("10 - Potenza")
        print("11 - Fattoriale")
        print("12 - Esponenziale")
        print("13 - Calcola quadrato")
        print("14 - Serie di Gauss")
        print("15 - Stampa su file")
        print("16 - Ripeti frase")
        print("17 - Scatter plot (grafico)")
        print("18 - Tavola numerica (LENTO: usa #30)")
        print("19 - Tavola numerica: quadrati perfetti")
        print("20 - Converti file in PDF")
        print("21 - Operazioni con le liste")
        print("22 - Lista quadrati")
        print("23 - Lista pari dispari")
        print("24 - Generatore di numeri casuali")
        print("25 - Calcola parallelepipedo GUI")
        print("26 - Insiemi random - operazioni tra insiemi")
        print("27 - Addizioni random (numero di cifre, punteggio, ...)")
        print("28 - Temperatura PC")     
        print("29 - Temperatura PC - grafico real time")
        print("30 - Tavola numerica CGPT (output su schermo, txt, pdf)")

        print("0 - Esci")

    while True:
        print()
        print("-----------")
        input("Premi un ENTER per mostrare il MENU: ...")
        menu_elenco()
        scelta = input("\nFai una scelta: ")


        if scelta == "1":
            calcola_cilindro()
        elif scelta == "2":
            calcola_cono()
        elif scelta == "3":
            calcola_parallelepipedo()
        elif scelta == "4":
            calcola_pitagora()
        elif scelta == "5":
            fibonacci()
        elif scelta == "6":
            insiemi()
        elif scelta == "7":
            validita_triangolo()
        elif scelta == "8":
            calcola_trapezio()
        elif scelta == "9":
            quadrato()
        elif scelta == "10":
            potenza()
        elif scelta == "11":
            fattoriale()
        elif scelta == "12":
            esponenziale()
        elif scelta == "13":
            calcola_quadrato()
        elif scelta == "14":
            serie_gauss()
        elif scelta == "15":
            stampa_su_file()
        elif scelta == "16":
            ripeti_frase()
        elif scelta == "17":
            scatter_plot()
        elif scelta == "18":
            tavola_numerica()
        elif scelta == "19":
            tavola_numerica_quad_perf()
        elif scelta == "20":
            file_in_pdf()
        elif scelta == "21":
            lista()
        elif scelta == "22":
            lista_quadrati()
        elif scelta == "23":
            lista_pari_dispari()
        elif scelta == "24":
            numeri_random()
        elif scelta == "25":
            apri_finestra()
        elif scelta == "26":
            insiemi_random()
        elif scelta == "27":
            somme_random()
        elif scelta == "28":
            get_cpu_temperature()
        elif scelta == "29":
            real_time_cpu_temp()
        elif scelta == "30":
            tavola_numerica_gpt()
        elif scelta == "0":
            break
        else:
            print("Scelta non valida. Riprova.")

def validita_triangolo():

    print("VALIDITÀ TRIANGOLO")

    a=input("Lato a: ")
    b=input("Lato b: ")
    c=input("Lato c: ")

    a=int(a)
    b=int(b)
    c=int(c)

    if b+c>a and c+a>b and a+b>c:
        
        if a==b==b==c:
            print("Equilatero")
        elif a==b or c==b or a==c:
            print("Isoscele")
        else:
            print("Scaleno")
    else:
        print("Triangolo non valido!!")
        if b+c<=a:
            print("b+c<=a")
        elif c+a<=b:
            print("c+a<=b")
        else:
            print("a+b<=c")
##########################

def calcola_pitagora():
    print("PITAGORA")
    incognita = input("Cosa vuoi calcolare? Cateto(C), Ipotenusa(I): ")
    ##while incognita!='C' or incognita!='I':
    ##    incognita = input("Cosa vuoi calcolare? Cateto(C), Ipotenusa(I)")

    while incognita !="C" and incognita !="I":
        print("Inserisci un dato corretto")
        incognita = input("Cosa vuoi calcolare? Cateto(C), Ipotenusa(I): ")


    if incognita=='C':
        cateto1=float(input("Cateto1: "))
        print()
        
        ipotenusa=float(input("Ipotenusa: "))

        while ipotenusa<=cateto1:
            ipotenusa=float(input("Ipotenusa deve essere maggiore del cateto: "))

        cateto2=float(math.sqrt(ipotenusa**2-cateto1**2))
        
        print("Cateto2 = radquad(",ipotenusa,"^2 - ", cateto1,"^2)")
        print("Cateto2 = radquad(",ipotenusa**2," - ", cateto1**2,")")
        print("Cateto2 = radquad(",ipotenusa**2-cateto2**1,")")
        print("Cateto2 = ",cateto2)

    elif incognita=='I':
        cateto1=float(input("Cateto1: "))
        cateto2=float(input("Cateto2: "))
        
        ipotenusa=float(math.sqrt(cateto1**2+cateto2**2))
        
        print("Ipotenusa = radquad(",cateto1,"^2 + ", cateto2,"^2)")
        print("Ipotenusa = radquad(",cateto1**2," + ", cateto2**2,")")
        print("Ipotenusa = radquad(",cateto1**2+cateto2**2,")")
        print("Ipotenusa = ",ipotenusa)
##############

def calcola_parallelepipedo():
    print("PARALLELEPIPEDO")
    larghezza=float(input("Inserisci la larghezza: "))
    profondita=float(input("Inserisci la profonà: "))
    altezza=float(input("Inserisci l'altezza: "))
    print()

    perimetro_base=2*larghezza+2*profondita
    print("Perimetro di base: ",perimetro_base)
    print()

    print("Altre aree laterali:")
    prof_per_alt= profondita*altezza
    print("Profondità x altezza: ",prof_per_alt)
    larg_per_alt= larghezza*altezza
    print("Larghezza x altezza: ",larg_per_alt)

    print()
    area_base=larghezza*profondita
    print("Area di base: \t",area_base)
    area_laterale=perimetro_base*altezza
    print("Area laterale: \t", area_laterale)
    area_totale=2*area_base+area_laterale
    print("Area totale: \t", area_totale)
    print()

    lunghezza_spigoli = larghezza*4 + profondita*4 + altezza*4
    print("Lunghezza complessiva di tutti gli spigoli: ", lunghezza_spigoli)
##############

def calcola_cilindro():

    print("CILINDRO")
    raggio=float(input("Inserisci raggio: "))
    altezza=float(input("Inserisci l'altezza: "))
    print()

    circonferenza_pi=2*raggio
    circonferenza=2*raggio*math.pi
    print("Circonferenza: ",circonferenza_pi,"*pi=",circonferenza)

    print()
    area_base_pi=raggio**2
    area_base=area_base_pi*math.pi
    print("Area base: ",area_base_pi,"*pi=",area_base)

    area_laterale_pi=circonferenza_pi*altezza
    area_laterale=area_laterale_pi*math.pi
    print("Area laterale: ",area_laterale_pi,"*pi=",area_laterale)

    area_totale_pi=area_base_pi+area_laterale_pi
    area_totale=area_totale_pi*math.pi
    print("Area totale: ",area_totale_pi,"*pi=",area_totale)

    print()
    volume_pi=area_base_pi*altezza
    volume=volume_pi*math.pi
    print("Volume: ",volume_pi,"*pi=",volume)

    ### stampa il cilindro
    with open("output.txt", "a") as file:
        # Redirect the print output to the file
        tempo = datetime.datetime.today()
        file.write("\n\n"+str(tempo)+"\n")
        file.write("Area base: "+str(round(area_base,2))+"\n"+
                   "Area laterale: "+str(area_laterale)+"\n"+
                   "Area totale: "+str(area_totale))
        print(datetime.datetime.today())

##############

def calcola_cono():
    print("CONO")
    occorrenze = ['raggio' in locals(), 'altezza' in locals(), 'apotema' in locals()]
    numero_occorrenze_vere = occorrenze.count(True)
    #print (numero_occorrenze_vere)

    print("CONO")
    print("Inserisci due valori a scelta, tra raggio, altezza e apotema")

    while numero_occorrenze_vere<2:
        cosa_conosci = input("Cosa conosci? raggio(r), altezza(h), apotema(a): ")
        if cosa_conosci == "r":
            raggio = float(input("Inserisci raggio: "))
        elif cosa_conosci == "h":
            altezza = float(input("Inserisci l'altezza: "))
        elif cosa_conosci == "a":
            apotema = float(input("Inserisci apotema: "))      

        occorrenze = ['raggio' in locals(), 'altezza' in locals(), 'apotema' in locals()]
        numero_occorrenze_vere = occorrenze.count(True)
        print("Valori inseriti: "+str(numero_occorrenze_vere))

        if 'apotema' in locals() and 'raggio' in locals():
            if raggio>=apotema:
                print()
                print("Il raggio non può esser maggiore o uguale all'apotema.")
                del raggio
                del apotema
                print("Tutte le variabili sono state cancellate, inseriscile di nuovo:.....")
        if 'apotema' in locals() and 'altezza' in locals():
            if altezza>=apotema:
                print()
                print("L'altezza non può esser maggiore o uguale all'apotema.")
                del altezza
                del apotema
                print("Tutte le variabili sono state cancellate, inseriscile di nuovo:.....")

        occorrenze = ['raggio' in locals(), 'altezza' in locals(), 'apotema' in locals()]
        numero_occorrenze_vere = occorrenze.count(True)

    print()
    print("DATI INSERITI:")
    if 'raggio' in locals():
        print("Raggio: ",raggio)
    if 'altezza' in locals():
        print("Altezza: ",altezza)
    if 'apotema' in locals():
        print("Apotema: ",apotema)

    print()
    print("SVOLGIMENTO:")
    if 'raggio' in locals() and 'altezza' in locals():
        apotema = math.sqrt(raggio ** 2 + altezza ** 2)
        print("Apotema: ", apotema)
    if 'apotema' in locals() and 'raggio' in locals():
        altezza = math.sqrt(apotema ** 2 - raggio ** 2)
        print("Altezza: ", altezza)
    if 'apotema' in locals() and 'altezza' in locals():
        raggio = math.sqrt(apotema ** 2 - altezza ** 2)
        print("Raggio: ", raggio)

    print()

    circonferenza_pi = 2 * raggio
    circonferenza = 2 * raggio * math.pi
    print("Circonferenza: ", circonferenza_pi, "*\u03C0 =", circonferenza)

    print()
    area_base_pi = raggio ** 2
    area_base = area_base_pi * math.pi
    print("Area base: ", area_base_pi, "*\u03C0 =", area_base)

    area_laterale_pi = apotema * raggio
    area_laterale = area_laterale_pi * math.pi
    print("Area laterale: ", area_laterale_pi, "*\u03C0 =", area_laterale)

    area_totale_pi = area_base_pi + area_laterale_pi
    area_totale = area_totale_pi * math.pi
    print("Area totale: ", area_totale_pi, "*\u03C0 =", area_totale)

    print()
    volume_pi = area_base_pi * altezza / 3
    volume = volume_pi * math.pi
    if round(volume_pi)-volume_pi<0.00000000001:
        print("Volume: ", round(volume_pi), "*\u03C0 =", volume)
    else:
        print("Volume: ", volume_pi, "*\u03C0 =", volume)

####
def fibonacci():
    a=0
    n=input("Calcola serie di Fibonacci del numero: ") 
    for i in range(int(n)):
        a=a+i
        print(i, a, "\t+", i+1)

####
#insiemi
def insiemi():
    print("INSIEMI:")
    a=input("Inserisci la stringa a: ")
##    print(a)
    a_set=set(a)
    print(a_set)

    print()
    b=input("Inserisci la stringa b: ")
##    print(b)
    b_set=set(b)
    print(b_set)

    input("")

    print()
    print("Intersezione a&b, a \u2229 b:")
    print(a_set&b_set)
    print()
    print("Unione a|b, a \u222a b: ")
    print(a_set|b_set)
    print()
    print("Differenza a-b: ")
    print(a_set-b_set)
    print()
    print("Elementi non in comune a^b: ")
    print(a_set^b_set)

### Trapezio
def calcola_trapezio():
    print("TRAPEZIO")
    base_1 = float(input("Inserisci base 1: "))
    base_2 = float(input("Inserisci base 2: "))
    altezza = float(input("Inserisci altezza: "))

    area = (base_1+base_2)*altezza/2
    print("Area: ",area)
                              
## Fattoriale
def fattoriale():
    print("FATTORIALE")
    print("Calcola il fattoriale n! di un numero n")
    n = int(input("Inserisci un numero intero: "))

    print("n","\t","n!")
    print("-------------------")
    for i in range(n):

        print(i,"\t", math.factorial(i))

## quadrato
def quadrato():
    print("QUADRATO")
    n = int(input("Inserisci un numero intero: "))
    print("n","\t","n^2")
    for i in range(n):
        print(i,"\t", i**2)

## potenza
def potenza():
    print("POTENZA")
    n = int(input("Inserisci un numero intero: "))
    e = int(input("Inserisci un esponente: "))
    for i in range(n):
        print(i,"\t", math.pow(i,e))

## esponenziale
def esponenziale():
    print("ESPONENZIALE")
    print("Calcola la potenza di un numero 'a', \n\
          con un esponente che va da '0' fino a 'n'")
    n = int(input("Inserisci un numero intero del massimo esponente: "))
    a = int(input("Inserisci numero intero \"a\" della base: "))
    
    print("n","\t"+str(a)+"^n")
    for i in range(n+1):
        print(i,"\t", math.pow(a,i))

## funzione di prova per il commit
def calcola_quadrato():
    
    scelta = input("Cosa conosci? \nSpigolo(l), \ndiagonale(d)\n")
    if scelta == "l":
        lato = float(input("Inserisci la misura del lato: "))
        diagonale = lato*math.sqrt(2)
    elif scelta == "d":
        diagonale = float(input("Inserisci la misura della diagonale: "))
        lato = diagonale/math.sqrt(2)
    else: 
        print("Dato inserito non corretto, riprova")
        calcola_quadrato()
    
    perimetro = lato * 4
    area = lato**2
    print("Perimetro =", perimetro)
    print("Area =", area)

def serie_gauss():
    print("SERIE DI GAUSS")
    n = int(input("Inserisci un numero del quale \
                  vuoi calcolare la serie di Gauss: "))

    minimo = 0
    serie_n = 0
    print("n\tSerieGauss(n)")
    for numero in range(n):
        serie_n = serie_n + minimo
        minimo +=1
        print(str(numero)+"\t"+str(serie_n))

    print("\n")
    # minimo = 0
    # serie_n = 0
    # for numero in range(n):
    #     serie_n = serie_n + minimo
    #     print("S",numero," = ", end="")
        
    #     if numero == 0:
    #         print("0")
    #     elif numero == 1:
    #         print("1")
    #     else:
    #         print("1", end='')
    #         for x in range(2,numero+1):
    #                 print(" +", x, end='')
        
    #         print(" =",serie_n)
        
    #     minimo+=1

def stampa_su_file():
    with open("output.txt", "a") as file:
        # Redirect the print output to the file
        testo=input ("cosa vuoi stampare?: ")
        file.write("\n")
        print(datetime.datetime.today())
        tempo = datetime.datetime.today()
        file.write("\n"+testo)
        file.write("\n"+str(tempo))
        # print(testo,file=file)
        # print("Hello, World!", file=file)
        # print("This is another line.", file=file)
        # print("And another one.", file=file)


def ripeti_frase():
    print("RIPETI FRASE")
    print("Ripete e scrive su un file (output.txt) una frase data")
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

def scatter_plot():

    print("SCATTER PLOT")
    print("Grafico con numerio casuali")
    x = np.random.randint(100, size=(100))
    y = np.random.randint(100, size=(100))
    colors = np.random.randint(100, size=(100))
    sizes = 10 * np.random.randint(100, size=(100))

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
    plt.colorbar()
    plt.show() 

def tavola_numerica_gpt():
    print("TAVOLA NUMERICA")
    print("Stampa la tavola numerica a video e sul file tavola_numerica.txt")
 
    while True:
        try:
            minimo = int(input("Inserisci un numero minimo della tavola: "))
            break
        except ValueError:
            print("Oops! Non è un valore numerico")

    while True:
        try:
            n = int(input("Inserisci un numero massimo della tavola: "))
            while n<minimo:
                while True:
                    try:
                        n = int(input(f"Inserisci un numero massimo della tavola, >= {minimo}: "))
                        break
                    except ValueError:
                        print("Oops! Non è un valore numerico")
            break
        except ValueError:
            print("Oops! Non è un valore numerico")


    n = int(input("Inserisci un numero massimo della tavola: "))
    while n<minimo:
        n = int(input(f"Inserisci un numero massimo della tavola, >= {minimo}: "))
    

    # Lunghezza massima stringhe
    len_n = len(str(n)) + 3
    len_n2 = len(str(n**2)) + 3
    len_n3 = len(str(n**3)) + 3
    len_radq = len(str(round(math.sqrt(n), 4))) + 3
    if len_radq < 12:
        len_radq = 12
    len_radc = len(str(round(n ** (1 / 3), 4))) + 3
    if len_radc < 12:
        len_radc = 12
    print(len_n,len_n2,len_n3,len_radq,len_radc)

    table_rows = []
    table_rows.append(f"{'n ':<{len_n}}{'n^2 ':<{len_n2}}{'n^3 ':<{len_n3}}{'rad_quad(n) ':<{len_radq}}{'rad_cub(n) ':<{len_radc}}")
    table_rows.append("---------------------------------------------------------------------------")

    for i in range(minimo, n + 1):
        n_quadrato = i ** 2
        n_cubo = i ** 3
        n_radquad = round(math.sqrt(i), 4)
        n_radcub = round(i ** (1 / 3), 4)

        row = f"{i:<{len_n}}{n_quadrato:<{len_n2}}{n_cubo:<{len_n3}}{n_radquad:<{len_radq}}{n_radcub:<{len_radc}}"
        table_rows.append(row)

    table = "\n".join(table_rows)
    
    print(table)

    nome_file = "tavola_numerica.txt"
    print("Printing txt file. Wait...")
    with open(nome_file, "w") as file:
        sys.stdout = file
        print(table)
        sys.stdout = sys.__stdout__ ## ripristina il normale output

    convert_to_pdf(nome_file)

def tavola_numerica():
    ## scrive su schermo
    print("TAVOLA NUMERICA")
    print("Stampa la tavola numerica a video e sul file tavola_numerica.txt")
    minimo = int(input("Inserisci numero minimo: "))
    n = int(input("Inserisci numero massimo: "))

    print("n" 
          + "\t" + "n^2" 
          + "\t\t" + "n^3" 
          + "\t\t" + "rad_quad(n)" 
          + "\t\t" + "rad_cub(n)")
    print("---------------------------------------------------------------------------")

    i = 0
    file_origine = "tavola_numerica.txt"
    for i in range(minimo, n+1):
        n_quadrato = i**2
        n_cubo = i**3
        n_radquad = round(math.sqrt(i), 4)
        n_radcub = round(i**(1/3), 4)

        print(str(i) 
              + "\t" + str(n_quadrato) 
              + "\t\t" + str(n_cubo) 
              + "\t\t" + str(n_radquad) 
              + "\t\t\t" + str(n_radcub))
        i=i+1


        ## Scrive la tavola su un file
        
        with open(file_origine, "w") as file:
            i = 0

            intestazione = ("n" 
                + "\t" + "n^2" 
                + "\t\t" + "n^3" 
                + "\t\t" + "rad_quad(n)" 
                + "\t\t" + "rad_cub(n)")
            
            file.write(intestazione + "\n")
            file.write("---------------------------------------------------------------------------\n")
            
            for i in range(minimo, n+1):
                n_quadrato = i**2
                n_cubo = i**3
                n_radquad = round(math.sqrt(i), 4)
                n_radcub = round(i**(1/3), 4)

                riga = (str(i) 
                    + "\t" + str(n_quadrato) 
                    + "\t\t" + str(n_cubo) 
                    + "\t\t" + str(n_radquad) 
                    + "\t\t\t" + str(n_radcub))

                file.write(riga)
                file.write("\n")

                i=i+1
            
    convert_to_pdf(file_origine)

## Output su file
def tavola_numerica_stdout():
    n = int(input("Inserisci fino a quale numero 'n' \
                  vuoi calcolare la tavola periodica: "))

    with open('tavola_sys.txt', 'w') as f:
        sys.stdout = f

        print("n" + "\t" 
              + "n^2" + "\t\t" 
              + "n^3" + "\t\t" 
              + "rad_quad(n)" + "\t\t" 
              + "rad_cub(n)")
        print("----------------------------------------------------------------")

        for i in range(n + 1):
            n_quadrato = i ** 2
            n_cubo = i ** 3
            n_radquad = round(math.sqrt(i), 4)
            n_radcub = round(i ** (1 / 3), 4)

            print('{0:2d}{1:3d}{2:4d}{3:5d}{4:6d}'.format(i,n_quadrato,n_cubo,n_radquad,n_radcub))
            
            # print(str(i) 
            #       + "\t" + str(n_quadrato) 
            #       + "\t\t" + str(n_cubo) 
            #       + "\t\t" + str(n_radquad).ljust(13) 
            #       + "\t\t\t" + str(n_radcub))
        
        sys.stdout = sys.__stdout__ ## ripristina il normale output
    
## output multipli (ci sono errori da correggere)
def tavola_numerica_tee():
    n = int(input("Inserisci fino a quale numero 'n' \
                  vuoi calcolare la tavola periodica: "))

    with open('tavola_sys.txt', 'w') as f:

        def write_output(line):
            print(line)
            print(line, file=f)
            #f.flush()  # Flush the file buffer to ensure immediate write
        
        sys.stdout = write_output

        print("n" + "\t" 
              + "n^2" 
              + "\t\t" + "n^3" 
              + "\t\t" + "rad_quad(n)" 
              + "\t\t" + "rad_cub(n)")
        print("----------------------------------------------------------------")

        for i in range(n + 1):
            n_quadrato = i ** 2
            n_cubo = i ** 3
            n_radquad = round(math.sqrt(i), 4)
            n_radcub = round(i ** (1 / 3), 4)

            print(str(i) + "\t" 
                  + str(n_quadrato) 
                  + "\t\t" + str(n_cubo) 
                  + "\t\t" + str(n_radquad).ljust(13) 
                  + "\t\t\t" + str(n_radcub))
        
        # ripristina il normale output
        sys.stdout = sys.__stdout__ 



def tavola_numerica_quad_perf():
    ## scrive su schermo
    print("TAVOLA NUMERICA - Quadrati perfetti")
    print("Stampa i quadrati perfetti della tavola numerica a video \
          e sul file tavola_numerica_quad_perf.txt")
    minimo = int(input("Inserisci numero minimo: "))
    n = int(input("Inserisci numero massimo: "))

    print("n" 
          + "\t" + "n^2" 
          + "\t\t" + "n^3" 
          + "\t\t" + "rad_quad(n)" 
          + "\t\t" + "rad_cub(n)")
    print("---------------------------------------------------------------------------")

    i = 0


    for i in range(minimo, n+1):
        n_quadrato = i**2
        n_cubo = i**3
        n_radquad = math.sqrt(i)
        n_radcub = i**(1/3)
        
        if n_radquad%2 == 0:
            print(str(i) 
                + "\t" + str(n_quadrato) 
                + "\t\t" + str(n_cubo) 
                + "\t\t" + str(round(n_radquad,4))
                + "\t\t\t" + str(round(n_radcub,4)))
            i=i+1

        ## Scrive la tavola su un file
        with open("tavola_numerica_quad_perf.txt", "w") as file:
            i = 0

            intestazione = ("n" 
                + "\t" + "n^2" 
                + "\t\t" + "n^3" 
                + "\t\t" + "rad_quad(n)" 
                + "\t\t" + "rad_cub(n)")
            
            file.write(intestazione + "\n")
            file.write("---------------------------------------------------------------------------\n")
            
            for i in range(minimo, n+1):
                n_quadrato = i**2
                n_cubo = i**3
                n_radquad = math.sqrt(i)
                n_radcub = i**(1/3)
                
                if n_radquad%2 == 0:
                    n_radcub = round(n_radcub, 4)

                    riga = (str(i) 
                        + "\t" + str(n_quadrato) 
                        + "\t\t" + str(n_cubo) 
                        + "\t\t" + str(n_radquad) 
                        + "\t\t\t" + str(n_radcub))

                    file.write(riga)
                    file.write("\n")

                    i=i+1

def file_in_pdf():
    
    def convert_to_pdf(input_file, output_file):
        try:
            pdfkit.from_file(input_file, output_file)
            print("File convetito in PDF con successo.")
        except Exception as e:
            print("Errore nella conversione:", str(e))
    
    input_file_path = input("Inserisci il percorso del file di input: ")
    output_file_path = input("Inserisci il percorso del fil di output: ")

    convert_to_pdf(input_file_path, output_file_path)


def convert_to_pdf(file):
    output_file = f"{file}.pdf"

    # Get the number of pages in the file (optional but useful for progress indication)
    page_count = pdfkit.from_file(file, output_file, options={'quiet': ''})

    # Print "Wait..." while the conversion is in progress
    print("Converting to PDF. Wait...Ci vuole pazienza")
    
    # Convert the file to PDF
    pdfkit.from_file(file, output_file, options={'quiet': ''})

    print(f"Conversion completed. PDF saved to {output_file}")


def lista():
    print("Operazioni con le liste")
    lista = ["melone", "pane", "aceto"]
    print("esempio di lista della spesa:")
    print(lista)
    print()

    print("Lunghezza della lista: "+ str(len(lista)))
    print()

    print("Primo elemento della lista: "+ lista[0])
    print("Ultimo elemento della lista: " + lista[len(lista)-1])
    print()

    print("Stampa ogni singolo elemento della lista e il suo index: ")
    indice = 0
    for elemento in lista:
        print(indice, elemento)
        indice = indice + 1
    print()

    lista_vuota = []
    print("Lista vuota:")
    print(lista_vuota)
    print()

    print("Aggiungi un elemento alla lista: lista.append(\"nome\")")
    nuovo_elemento = input("Scrivi elemento: ")
    lista.append(nuovo_elemento)
    print(lista)
    print()

    print("Cancella un elemento con un dato indice: \
          del lista[indice_elemento] ")
    indice_elemento = int(input("Indice elemento: "))
    del lista[indice_elemento]
    print(lista)
    print()

    print("Cancella elemento dato il suo nome: lista.remove(\"nome\")")
    elemento = input("Elemento da cancellare: ")
    lista.remove(elemento)
    print(lista)
    print()

    print("Aggiunge alcuni elementi numerici")
    elemento = 0
    for elemento in range(10):
        lista.append(elemento)
        elemento = elemento + 1
    print(lista)
    print()

    print("Rimuove l'usltimo elemento e ritorna la lista \
          con l'elemento rimosso: lista.pop()")
    for pop in range(len(lista)):
        popped = lista.pop()
        print(lista)

def lista_spesa():
    print("LISTA DELLA SPESA")
    print("Scrivi la tua lista della spesa")
    
    elemento = ""
    lista_spesa = []
    while elemento != "fine":
        elemento = input("Inserisci un elemento nella lista \
                         (\"digita 'fine' per terminare\"): ")
        if elemento != "fine":
         lista_spesa.append(elemento)
    
    print()
    print("Lista della spesa:")
    print(lista_spesa)
    print()

    print("Ordina in ordine alfabetico crescente: lista.sort()")
    lista_spesa.sort()
    print(lista_spesa)
    print()

def lista_quadrati():
    print("QUADRATI DI UNA LISTA DI NUMERI")
    print("Calcola il quadrato di una lista di numeri dati: \
          squares = [x**2 for x in lista]")
    print()

    elemento = ""
    lista = []
    while elemento != "fine":
        elemento = input("Inserisci un numero nella lista  \
                         (\"digita 'fine' per terminare\"): ")
        if elemento != "fine":
         lista.append(elemento)
    
    print()
    print("Lista di numeri:")
    print(lista)
    print()

    indice = 0
    for elemento in lista:
        elemento = int(elemento)
        lista[indice] = elemento
        indice = indice + 1

    squares = [x**2 for x in lista]
    print("Lista quadrati: ")
    print(squares)

def lista_pari_dispari():
    print("LISTA PARI DISPARI")
    print("Data una lista di numeri, \nrestituisce una lista di quelli PARI \
           e una lista di quelli DISPARI")

    elemento = ""
    lista = []
    while elemento != "fine":
        elemento = input("Inserisci un numero nella lista \
                         (\"digita 'fine' per terminare\"): ")
        if elemento != "fine":
            lista.append(elemento)
    
    indice = 0
    for elemento in lista:
        elemento = int(elemento)
        lista[indice] = elemento
        indice = indice + 1
    
    print()
    print("Lista di numeri:")
    print(lista)
    print()

    input( "Premi INVIO")
    pari = [x for x in lista if x % 2 == 0]
    print("Pari:")
    print(pari)
    print()

    input( "Premi INVIO")
    dispari = [x for x in lista if x%2 != 0]
    print("Dispari:")
    print(dispari)
    print()

def numeri_random():
    print("GENERATOR DI NUMERI CASUALI")
    print()
    numero_minimo = int(input("Inserisci nuemro minimo: "))
    numero_massimo = int(input("Inserisci numero massimo: "))
    ammesse_ripetizioni = input("Ammesse ripetizioni? Si 's', No 'n': ")
    if ammesse_ripetizioni == "n":
        totale_max_ammesso = numero_massimo - numero_minimo + 1
        totale_numeri = int(input("Numeri da restituire, massimo " 
                                  + str(totale_max_ammesso) + ": "))
        while totale_numeri > totale_max_ammesso:
            totale_numeri = int(input("Inserisci di nuovo!!\n\
                                      Numeri da restituire, massimo " \
                                      + str(totale_max_ammesso) + ": "))
    elif ammesse_ripetizioni == "s":
        totale_numeri = int(input("Numeri da restituire: "))
    print()

    if ammesse_ripetizioni == "n":
        numeri = random.sample(range(numero_minimo, 
                                     numero_massimo+1), 
                                     totale_numeri)
    elif ammesse_ripetizioni == "s":
        numeri = random.choices(range(numero_minimo, 
                                      numero_massimo+1), 
                                      k=totale_numeri)

    print(numeri)

    i = 1
    for numero in numeri:
        print(i,numero)
        i = i+1


def apri_finestra():
    def calcola_parallelepipedo_gui():
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
    button_calculate = tk.Button(window, 
                                 text="Calculate", 
                                 command=calcola_parallelepipedo_gui)
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

def insiemi_random():
    print("INSIEMI RANDOM")

    totale_numeri = int(input("Inserisci la lunghezza degli insiemi: "))
    minimo = int(input("Valore minimo: "))
    massimo = int(input("Valore massimo: "))

    a = random.sample(range(minimo, massimo), totale_numeri)
    b = random.sample(range(minimo, massimo), totale_numeri)
    a = set(a)
    b = set(b)
    print("a = ", a)
    print("b = ", b)

    insiemi_operazioni(a,b)

def insiemi_operazioni(a,b):
    print("OPERAZIONI TRA DUE INSIEMI")
    print()
    print("INTERSEZIONE a&b, a \u2229 b:")
    input()
    print(a&b)
    
    print()
    print("UNIONE a|b, a \u222a b: ")
    input()
    print(a|b)
    
    print()
    print("DIFFERENZA a-b: ")
    input()
    print(a-b)
    
    print()
    print("ELEMENTI NON IN COMUNE a^b: ")
    input()
    print(a^b)

    #return a,b

## Chat GPT version
 
def generate_addition_problem(max_value1, max_value2):
    addend1 = random.randint(0, max_value1)
    addend2 = random.randint(0, max_value2)
    return addend1, addend2

def check_answer(addend1, addend2, answer):
    expected_result = addend1 + addend2
    return answer == str(expected_result)

def somme_randomp_gpt():
    print("ADDIZIONI RANDOM")

    max_value1 = int(input("Massimo valore del primo addendo 'a': "))
    max_value2 = int(input("Massimo valore del secondo addendo 'b': "))
    print()

    correct_answers = 0
    total_questions = 0

    while True:
        addend1, addend2 = generate_addition_problem(max_value1, max_value2)
        result = addend1 + addend2

        print("Digita il risultato corretto o 'fine' per terminare")
        print("ES:", total_questions + 1)
        print(f"{addend1} + {addend2} = ", end='')
        answer = input()

        if answer == "fine":
            break

        if check_answer(addend1, addend2, answer):
            print("Corretto!")
            correct_answers += 1
        else:
            print("Errato! Il risultato corretto era", result)

        total_questions += 1

    percentage_correct = (correct_answers / total_questions) \
                        * 100 if total_questions > 0 else 0

    print("Domande:", total_questions)
    print("Risposte esatte:", correct_answers)
    print("Percentuale esatte:", percentage_correct, "%")

########################### fine chat gpt

def somme_random():
    print("ADDIZIONI RANDOM")
    print("Verifica e stampa i risultati sotto forma di \
          report nel file '27 - Report risultati'")

    

    nome = input("Inserisci il tuo nome: ")

    # gestione delle eccezioni nelle cifre degli addendi:
    while True:
        try:
            massimo_a = int(input("Massimo valore del primo addendo 'a': "))
            break
        except ValueError:
            print("Oops! Non è un valore numerico valido. Ritenta ...")

    while True:
        try:
            massimo_b = int(input("Massimo valore del secondo addendo 'b': "))
            break
        except ValueError:
            print("Oops! Non è un valore numerico valido. Ritenta ...")
    print()

    # inizializzazione variabili
    risposte_esatte = 0
    numero_domande = 0
    contatore = 1
    esito = ""
    prima_risposta = ""
    risposta = ""
    lista_domande = []
    lista_tempi_es = []
    tempo_inizio = datetime.datetime.today()

    print(f"Orario inizio: {tempo_inizio}")

    while risposta != "fine":
        tempo_inizio_es = datetime.datetime.today()
        operators = ['+', '-', '*', '/']
        selected_operator = random.choice(operators)
        
        a = random.randint(a=0, b=massimo_a)
        b = random.randint(a=0, b=massimo_b)
        risultato = a + b

        print("ES: ",numero_domande + 1)
        print("Digita il risultato corretto o 'fine' per terminare")
        print(f"{a} + {b} = ", end='')
        risposta = input("")

        if risposta == "fine":
            esito = "errato"
            contatore = 0       
            
        elif risposta == str(risultato):
            tempo_fine_es = datetime.datetime.today()
            print("Corretto!!")
            esito = "corretto"
            contatore = 1
            prima_risposta = risposta

        else:
            tentativi = 1

            while risposta != str(risultato):
                if risposta == "fine":
                    esito = "errato"
                    contatore = 0
                    prima_risposta = risposta

                else:
                    while risposta != "salta" \
                    and risposta !=str(risultato) \
                    and risposta != "fine":
                        risposta = input("ERRATO, ritenta \
                                         \no digita 'salta' per andare aventi,\
                                         \n 'fine' per terminare: ")
                        esito = "errato"
                        contatore = 1
                        tentativi = tentativi + 1
                        tempo_fine_es = datetime.datetime.today()
                    break
            
            if risposta == str(risultato):
                print("Corretto, dopo ",tentativi, "tentativi")
                tempo_fine_es = datetime.datetime.today()
        
        print()

        ## tempi singolo es:
        tempo_impiegato_es = tempo_fine_es - tempo_inizio_es
        
        lista_tempi_es.append(tempo_impiegato_es)

        if esito == "corretto":
            risposte_esatte = risposte_esatte + 1

        # Aggiornamento contatori
        numero_domande = numero_domande + contatore
        percentuale_corrette = risposte_esatte / numero_domande * 100
        
        # aggiunge operazione alla lista domande
        lista_domande.append(f"ES.{numero_domande}: {a} + {b} = {risultato} \n\
                              {esito}: la prima risposta è stata {prima_risposta}")

    print()
    def esiti():
            print("---------------------------------------------------------")
            print()
            print("REPORT esiti:")
            tempo_fine = datetime.datetime.today()
            print(f"Orario di fine: {tempo_fine}")
            print()
            
            i = 0
            for elemento in lista_domande:
                print(f"{elemento}, tempo impiegato: {lista_tempi_es[i]}")
                i = i+1
            print()

            # Candidato
            print(f"Candidato: {nome}\n")

            ## Report
            # Tempi
            tempo_fine = datetime.datetime.today()
            tempo_impiegato = tempo_fine - tempo_inizio
            media_tempo_impiegato = tempo_impiegato / numero_domande
            print(f"Orario inizio: {tempo_inizio}")
            print(f"Orario fine: {tempo_fine}")
            print(f"Tempo impiegato: {tempo_impiegato}")
            print(f"Media tempo impiegato, singolo es.: {media_tempo_impiegato}")
            print()

            # Report Statistiche domande
            print("Domande: ", numero_domande)
            print("Risposte esatte: ", risposte_esatte)
            print("Percentuale esatte: ", round(percentuale_corrette, 2), "%")

    esiti()
    with open("27 - Report risultati.txt", "a") as file:
        ## stampa la lista domande
        sys.stdout = file
        esiti()
        # ripristina il normale output
        sys.stdout = sys.__stdout__ 

def parallelepipedo_classe():
    print("PARALLELEPIPEDO (Classe e oggetti)")

    par1 = ParallelepipedoRetto(1,2,3)
    # (int(input("larghezza: ")), 
    # int(input("Profondità: ")), 
    # int(input("Altezza: ")))

    par1.area_base()
    par1.area_laterale()
    par1.calcola_volume()

    par2 = ParallelepipedoRetto(2,3,4)

    par2.area_base()
    par2.area_laterale()
    par2.calcola_volume()

    print(par1._larghezza/ par2._larghezza)

    print(par1)

    print(ParallelepipedoRetto.NUMERO_SPIGOLI)

    par1.set_larghezza(-12.5)
    print(par1._larghezza)


## Temperatura computer
def get_cpu_temperature():
    while True:
        temperature = psutil.sensors_temperatures()

    
        if "coretemp" in temperature:
            # Assuming coretemp provides per-core temperature
            core_temps = temperature["coretemp"]
            for temp in core_temps:
                # Print the temperature of each core
                print(f"Core {temp.label}: {temp.current}°C")
        else:
            print("CPU temperature information not available.")
    time.sleep(1)

def real_time_cpu_temp():
    # Set the maximum number of data points to display in the real-time diagram
    max_data_points = 1000

    # Initialize lists to store timestamps and temperature values
    timestamps = []
    temperatures = []

    # Create a figure and axes for the plot
    fig, ax = plt.subplots()

    # Set the axis labels
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')

    # Set the plot title
    ax.set_title('Real-Time Temperature - Core 0')

    # Create an empty line object for the plot
    line, = ax.plot(timestamps, temperatures)

    # Set the y-axis limits
    ax.set_ylim(0, 100)  # Modify the limits according to your temperature range

    # Function to update the plot with new temperature data
    def update_plot():
        # Retrieve the temperature for core 0
        temperature = psutil.sensors_temperatures()['coretemp'][1].current

        # Append the current timestamp and temperature to the lists
        timestamps.append(len(timestamps))
        temperatures.append(temperature)

        # Keep only the last 'max_data_points' data points
        if len(timestamps) > max_data_points:
            timestamps.pop(0)
            temperatures.pop(0)

        # Update the plot data
        line.set_data(timestamps, temperatures)

        # Adjust the x-axis limits to fit the data
        ax.set_xlim(0, max(timestamps) + 1)

        # Redraw the plot
        fig.canvas.draw()

    # Call the update_plot() function periodically to update the plot
    timer = fig.canvas.new_timer(interval=1000)  # Update the plot every second (adjust as needed)
    timer.add_callback(update_plot)
    timer.start()

    # Display the plot
    plt.show()




###############################


menu()