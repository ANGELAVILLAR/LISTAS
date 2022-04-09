#Construir lista que sustituya cualquier NEGATIVO en cero

n=[]
lista=int(input('Ingrese los valores de la lista:'))

for i in range(1,n):
    if i < 0:
        print('Por favor incluya valores positivos en la lista')
else:
    if i > 0:
        print(f' {n}, end','')
        

