#print("ingrese la calificcion 1")
Cal1=input("ingrese la calificcion 1:")
#print("ingrese la calificacion 2")
Cal2=input("ingrese la calificcion 2:")
#print("ingrese la calificacion 3")
Cal3=input("ingrese la calificcion 3:")
if(Cal1.isdigit() and Cal2.isdigit() and Cal3.isdigit()):
    Prom=(int(Cal1)+int(Cal2)+int(Cal3))//3
    if(Prom>=4):
        print("Aprueba")
    else:
        print("Suspende")
    #fin if
    print(Prom)
else:
    print("Porfavor entre calificaciones con numeros enteros")
#fin Aprueba_suspende
