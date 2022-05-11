class Persona:
    Nombres=""
    Apellidos=""

    def __init__(self,nombres,apellidos):
        self.Nombres=nombres
        self.Apellidos=apellidos
    def __str__ (self):
        return "{} {} ".format(self.Nombres,self.Apellidos)
    def caminar(self):
        print ("caminando")
a=1   
profesor= Persona("Billy","Vanegas")
#profesor.Nombres="Billy" #SETTER
#profesor.Apellidos="Vanegas"

print(type(profesor.Nombres))

alumno = Persona("Pedro","Sanchez")
#alumno.Nombres="Pedro"
#alumno.Apellidos="Alvarez"

alumno1 = Persona("Mario","Villar")
#alumno1.Nombres="Mario"
#alumno1.Apellidos="Villar"

administrativo= Persona("Juan","Perez")
#administrativo.Nombres= "Juan"
#administrativo.Apellidos= "Perez"

#AL INTRODUCIR LINEA 6,7 LAS LINEAS 14 15 NO SON NECESARIAS

#a=1
#print(type(a))
print("El profesor: {} {}".format(profesor.Nombres,profesor.Apellidos))  #GETTER
print("El alumno: {} {}".format(alumno.Nombres,alumno.Apellidos))
print("El alumno1: {} {}".format(alumno1.Nombres,alumno1.Apellidos))
print("El administrativo: {} {}".format(administrativo.Nombres,administrativo.Apellidos))
print("El alumno:",alumno)
profesor.caminar()

