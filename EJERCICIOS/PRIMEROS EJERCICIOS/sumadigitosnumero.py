#Algoritmo SumaDigitos
	nro = input ("Ingrese un nro: ")
    resul = 0
	while nro ≠ 0:
	    resul = resul + (nro % 10)
        nro= nro//10
	Mientras nro <> 0 Hacer
		resul <- resul + nro MOD 10
		nro <- trunc(nro/10)
	#FinMientras
	print "El resultado es: " resul
#FinAlgoritmo