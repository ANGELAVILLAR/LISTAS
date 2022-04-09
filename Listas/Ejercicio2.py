#Construya un programa que almacene en una lista obtenida con lista(range(1,n))
#Donde n es un entero desde teclado
#Modificar lista para que cada componente sea igual al cubo del componente original
#Mostrar lista en pantalla

lista=[]
n=int(input("Ingrese el tamaño de la lista: "))

for i in range(1,n):
    cubo = i**3
    lista.append(cubo)
print(lista)


