#ejer 1
""""
lst1=[1,2,3,4,5]
lst2=[]
#for n in list1:
#   lst.append(n)
lst2=[n for n in lst1]
print(lst2)
"""
#ejer2
"""
rng=[]
#for n in range(1200,2001,130):
#   rng.append(n)
#print(rng.__st)
#print(rng[1])
#print(list(rng))
#lst=[]
#for x in rng:
#    lst.append(x)
lst=[]
for x in rng:
    lst.apppend(x)

rng=range(1200,2001,130) #es quivalente a las lineas 11 12 13
lst=[x for x in rng]       #es equivalente a las lineas 17 18 19
print(lst)               #igual a linea 21
"""
#Ejer 3

""""

lst1=[44,54,64,74,104]
lst2=[]
for n in lst1:
    lst2.append(n+6)
print(f"version larga:lista 1: {lst1}\nLista 2: {lst2}")

lst1=[44,54,64,74,104]
lst2=[n+6 for n in lst1] #equivale a 34 35 36
print(f"version cota:lista 1: {lst1}\nLista 2: {lst2}")
"""

#ejer 4
"""
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[(num**2) for num in lst1]
print(lst2)

"""
#ejer 5
""""
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[]
for x in lst1:
    if (x**2)>50:
        lst2.append(x**2)
print(lst2)
lst2=[(x**2)for x in lst1 if (x**2)>50]
print(lst2)
"""
#ejer6
"""
dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
lst=[n.upper() for n in dict if dict[n]<1300]
print(lst)
"""
#ejer7
"""
#dict={"NY": "Nueva York", "FL": "Finlandia", "CA": "Canada", "VT": "Vietnam"} 
lst=["NY", "FL", "CA", "VT"]
#version larga
dict={}
for n in lst:
    #dict.setdefault(n,n)
    dict[n]=n
print(dict)
#version corta con comprension de listas
dict={x:x for x in lst}
print(dict)
"""
#Ejer8
"""
rng=range(100,161,10)
#version lista compresion
dict={x:(x/100) for x in rng}
print(dict)
#version larga
dict={}
for x in rng:
    dict[x]=(x/100)
print(dict)
"""
#Ejercicio 9
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
for n in dict1:
    if dict1[n]>2000:
        dict2[n]=dict[n]
print(dict2)        
dict2={x:dict1.get(x) for x in dict1 if dict1.get(x) > 2000}
print(dict2)

