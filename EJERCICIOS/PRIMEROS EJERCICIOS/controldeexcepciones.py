numero1=100
numero2=3
a="2"

try:
    print("otra instruccion1")
    print("otra instruccion2")
    print("otra instruccion3")
    print("otra instruccion4")
    print(numero1/numero2)
    print("otra instruccion5")
    c=int(a)
    print("otra instruccion6")
    print("otra instruccion7")
except ZeroDivisionError:
    print("Error al dividir por cero")

except:
    print("Error")
else:
    print("Las instrucciones se completaron en su totalidad")

finally: 
    print("fin de programa")

