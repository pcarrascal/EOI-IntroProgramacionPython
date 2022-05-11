#NumerosPrimos
numerodeprimos= input("Numero de primos a mostrar:")
if (numerodeprimos.isdigit()):
    numerodeprimos=int(numerodeprimos)  #Convertir la entrada de tipo TEXTO "3" a numero 3
    #iteracion
    #for nro in range(1,numerodeprimos):    #numerodeprimos= 1 hasta numerodeprimos<(nro)y paso 1
                                            #for no es util porque no mostrara los N numeros primos
                                            #contador =1 hasta que contador ==numerodeprimos cada primo suma contador haga
    nro=1                                   #mientras que numerodeprimos > 0(caad primo restaNumerodeprimos)
    while numerodeprimos >0:  
        div= 2
        band =True 	 #Boolean para comprobar si el numero es primo o no        
        if nro==1 : 		            
                print(f"{nro}Es primo") 
                numerodeprimos-=1	         
        else:
            while band and (nro>div) :
                if (nro % div) == 0 :
                    band = False
                    break
                #FinSi
                div += 1 #div = div +1
            #FinMientras
            if band:         #band==True equivalente band
                print("Es primo")
            else:
                print("No es primo")
            #FinSi
        #FinSi
else: 
    print('Por favor entre un numero valido')