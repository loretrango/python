## tutti le forme di geometria solida

import math
import modulo
from modulo import *
richiesta = ""

##
print("Lista di tutte le funzioni disponibili:")
# List functions of the module
functions = [func for func in dir(modulo) if callable(getattr(modulo, func))]

# Print the list of functions
for function in functions:
    print(function)

print()

##


menu()


print("Programma terminato")
#    

