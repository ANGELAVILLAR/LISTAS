# Defina una lista con los meses del año OK
# Defina una lista vacia OK
# Llenar la segunda lista con los datos de usuario
# Imprimir el promedio del año
# El mes y valor de mayor y menor produccion
# Mes por encima del promedio
# MEs por debajo del promedio

meses=['Enero','Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
listv=[]
for i in meses:
    ventas=int(input(f'Ingrese las ventas del mes {i}: '))
    ventas1 = listv.append(ventas)

print(ventas1)

diccionario = { meses[0]:listv[0],meses[1]:listv[1],meses[2]:listv[2], meses[3]:listv[3], meses[4]:listv[4], meses[5]:listv[5], meses[6]:listv[6], meses[7]:listv[7], meses[8]:listv[8], meses[9]:listv[9], meses[10]:listv[10], meses[11]:listv[11] }

print(diccionario)


