from operator import truediv


def saludar(nombre):
    #funcionalidad del tiempo o lo que queramos que siga al nombre
    print(f'Hola {nombre}, Buenos dias')

def sumar(a,b):
    return(a+b)

def addColores(colores,color):
    try:
        colores.append(color)
        return True
    except AttributeError:
        return False

saludar('Paula')
saludar('Belen')
saludar('Miguel')
saludar('Juan')
#ES LO MISMO QUE IR PONIENDO LA FUNCION EN CADA LINEA
#nombre='Paula'
#print(f'hola {nombre}')

print(sumar(5,5))
print(sumar(7,5))
print(sumar(4,5))
print(sumar(5,3))
print(sumar(5,1))

colores=[]
addColores(colores,'Azul')
addColores(colores,'Blanco')
addColores(colores,'Naranja')
addColores(colores,'Amarillo')
addColores(colores,'Rosa')
saludar (colores)


if (addColores('Paula','Naranja')): #Equivalente addCo..()==True linea 13
    print('Insertado color')
else:
    print('No insertado color')

if (addColores(colores,'Naranja')): #Esto haria la funicion correcta
    print('Insertado color')
else:
    print('No insertado color')

ciudad='Malaga'
ciudad