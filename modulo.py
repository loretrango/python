import math
import numbers


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
    print("Profondità per altezza: ",prof_per_alt)
    larg_per_alt= larghezza*altezza
    print("Larghezza per altezza: ",larg_per_alt)

    print()
    area_base=larghezza*profondita
    print("Area di base: \t",area_base)
    area_laterale=perimetro_base*altezza
    print("Area laterale: \t", area_laterale)
    area_totale=area_base+area_laterale
    print("Area totale: \t", area_totale)

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

##    print('raggio' in locals())
##    print('altezza' in locals())
##    print('apotema' in locals())


    print()
    print("SVOLGIMENTO:")

    ##if 'raggio' in locals():
    ##    if 'altezza' in locals():
    ##        apotema = math.sqrt(raggio ** 2 + altezza ** 2)
    ##        print("Apotema: ", apotema)
    ##    elif 'apotema' in locals():
    ##        altezza = math.sqrt(apotema ** 2 - raggio ** 2)
    ##        print("Altezza: ", altezza)
    ##if 'apotema' in locals():
    ##    if 'altezza' in locals():
    ##        raggio = math.sqrt(apotema ** 2 - altezza ** 2)
    ##        print("Raggio: ", raggio)
    ##        
    ##print("##")

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
# fibonacci
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

#### MENU
def menu():
    print("MENU")
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

    print("0 - Esci")

    while True:
        print()
        print("-----------")
        scelta = input("Fai una scelta: ")
        
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
        elif scelta == "0":
            break
        else:
            print("Scelta non valida. Riprova.")
                              
## Fattoriale
def fattoriale():
    print("FATTORIALE")
    n = int(input("Inserisci un numero intero: "))

    for i in range(n):

        print(i,"\t", math.factorial(i))

## quadrato
def quadrato():
    print("QUADRATO")
    n = int(input("Inserisci un numero intero: "))
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
    n = int(input("Inserisci un numero intero del massimo esponente: "))
    b = int(input("Inserisci numero intero della base: "))
    for i in range(n+1):
        print(i,"\t", math.pow(b,i))
