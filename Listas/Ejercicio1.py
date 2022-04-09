#Lista desde list(range(1,5)) 
#Modificar para que la lista sea igual al cuadrado del componente original.
#Imprimir la lista obtenida en pantalla

a=list(range(1,5))
number=[]

for i in a:
    r = i **2
    number.append(r)
print(number)

