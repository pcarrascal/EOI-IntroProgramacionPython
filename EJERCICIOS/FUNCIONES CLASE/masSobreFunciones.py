def ProcesoInicial():
    print('Buscar una hoja de papel')

def ProcesoDos():
    print('Doblar la hoja')

def SaludarAtodos(*nombres):
    for i in nombres:
        print (f'hola:{i}')

def SaludarAtodosDict(**nombres):
    for i in nombres:
        print(f'hola:{i} {nombres[i]}')

def Ciudades(pais,ciudad='Madrid'):
    print(pais,'',ciudad)
    

ProcesoInicial()
ProcesoDos()

SaludarAtodos('Paula')
SaludarAtodos('Belen','Miguel','Sofia')
SaludarAtodos('Laura','Juan','Maria')
SaludarAtodos()

SaludarAtodosDict(nombre='Paula', apellidos="Carrascal")

Ciudades('Malaga')
Ciudades('Mexico','Ciudad de Mexico')
Ciudades('Colombia', 'Bogota')