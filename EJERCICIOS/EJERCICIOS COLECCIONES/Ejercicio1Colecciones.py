from random import randint

#def contarpersonas(genero,coleccion)
personas=[]
for n in range(1,101):
    genero=randint(0,1) #0 para chicas y el 1 para chicos
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
print(personas)
no_chicos=personas.count("H")
no_chicas=personas.count("M")

if (no_chicos == no_chicas):
    print("Hay igualdad entre chicos y chicas")
elif no_chicos>no_chicas:
    print("Hay mas chicos que chicas")
else:
    print("Hay mas chicas que chicos")

print('El numero de chicos es :{0}% y el nuemro de chicas es:{1}%'.format(no_chicos,no_chicas))