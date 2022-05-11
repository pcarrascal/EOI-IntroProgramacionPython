def Fibonacci(N):

    if(N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return Fibonacci (N-1) + Fibonacci (N-2)

n=input("Introduce la posicion de fivonnaci: ")
try:
    n=int(n)
    serie_fibonacci=[]
    for i in range(1,n+1):
        r=Fibonacci(i)
        serie_fibonacci.append(r)
    print(f"el numero en esa posicion es: {r}")
    print('La serie es:',*serie_fibonacci)
except TypeError:
    print("Numero no valido")
except ValueError:
    print("Numero invalido")
except:
    print("fallo")














