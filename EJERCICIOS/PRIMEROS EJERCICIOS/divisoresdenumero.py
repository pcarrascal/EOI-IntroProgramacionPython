print("ingrese numero")
Num=input()
if (Num.isdigit()):
    Num=int(Num)
    div=1
    while(div<=Num):
        if (Num%div == 0):
            print(div)
        #Fin si
        div=div+1
    #Fin While
else:
    print("Por favor entre un numero valido")

#Fin divisores_de_numero
