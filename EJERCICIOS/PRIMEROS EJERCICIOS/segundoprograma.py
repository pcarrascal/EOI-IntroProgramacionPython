#Asignacion simultanea

a=5
b=10
print("paso1. Valores iniciales")
print(a)
print(b)
c=b
b=a
a=c
del c
print("paso 2. Valores intercambiados")
print(a)
print(b)

