#3 - Paridad numero
#print("ingrese un numero")
nro=input("ingrese un numero")
if (nro.isdigit()):
    nro=int(nro)
    if (nro%2==0):
        print("Es par")
    else:   
        print("Es impar")
else:
    print("Por favor entre un numero valido")
    24