list = []

n = 383883

n=int( input("inserisci numero: "))
print("Numero: ")
print(n)
print()

a = n
print("quoziente","\t","resto")
while a > 0:
	resto = a % 2
	a = a//2
	list.append(resto)
	print(str(a), "\t", str( resto))

print()
print("Lista:")		
print(list)

print("Lista invertita:")
list_reverse = list [::-1]
print(list_reverse)

print()
print("Numero binario:")
for element in list_reverse:
	print(str(element),end='')


print()