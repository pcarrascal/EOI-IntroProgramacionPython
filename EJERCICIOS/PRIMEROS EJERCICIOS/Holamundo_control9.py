#HOLA MUNDO
print ("HOLA MUNDO")


#Control numero 9

#N=0
print("Escribir el numero")
N=input() #N=VALOR"
if (N.isdigit()):
    N=int(N)
    if (N==9):
        print ("El numero es igual a 9")
    else:
        if (int(N)>9):
            print ("El numero es mayor a 9")
        else:
            print ("El numero es menor a 9")
        #Fin Si
    #Fin Si 
else:
     print("Por favor entre un valor numerico")  
#Fin Control Numero 9
