from sqlite3 import Cursor


class Persona:
    def __init__(self,nombres,apellidos):
        self.Nombres = nombres
        self.Apellidos= apellidos

class Alumno(Persona):
    Curso=None
    def __init__(self,nombres,apellidos,curso):
        self.Curso= curso
        super().__init__(nombres,apellidos)

est=Alumno('Paula','Carrascal','Cloud computing')
print(f':{est.nombres} {est.apellidos} {est.curso}')