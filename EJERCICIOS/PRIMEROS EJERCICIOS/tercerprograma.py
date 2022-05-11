ciudad="madrid"
print(ciudad.isdigit)

minombre="paula"
print(len(minombre))

print(minombre[0])
print(minombre[1])
print(minombre[4])
#print(minombre[5]) Error out of index
print(minombre[2:])
print(minombre[:3])
print(minombre[2:4])
print(minombre[-2])
print(minombre[1:10])

mensaje= "dd"
ciudad= "albacete"
print("hola {}".format(mensaje))
print("hola "+mensaje)

print("hola {m} de {c}".format(m=mensaje,c=ciudad))
#print ("hola "+mensaje) no es una forma eficiente de concatenar cadenas de caracteres

numero = 10/3
print("El numero sin formato es: {}".format(numero))

print("el numero con formato es:{n:1.2f}.format(numero")

print(f"Hola {mensaje} de {ciudad}")

