x=int(6)   #Numero dado

print("Introducir un numero")
y=(input())
if (y.isdigit()):
    y=int(y)
    if(x>y):
        print(f"{x} mayor o igual a  {y}")

    else:
        print (f"{y} mayor o igual a {x}")
else:
    print('Entre un numero valido')
