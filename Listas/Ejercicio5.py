#Diseñe un programa que lea una cadena
#Muestre en una lista con todas sus palabras en mayuscula
#Devuelva no debe tener palabras repetidas


texto=str(input('Ingresa el texto: '))

texto_mayuscula= texto.swapcase()
lista_texto= texto_mayuscula.split(' ')
lista1=list(set(lista_texto))
print(lista1)

