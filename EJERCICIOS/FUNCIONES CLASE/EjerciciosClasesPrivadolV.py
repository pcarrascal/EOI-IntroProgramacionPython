class Vehiculo:
    #METODO _privado
    def __privado(self):
        print("Soy privado") #privado es: utlizar esto dentro de a clase
    def metodo_publico(self):
        print("Soy un metodo publico") #utilizado fuera y dentro de la clase

g1 = Vehiculo()
#g1.__privado()
g1._Vehiculo__privado()
g1.metodo_publico()

