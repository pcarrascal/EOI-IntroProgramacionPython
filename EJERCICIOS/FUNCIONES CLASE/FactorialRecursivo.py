def Factorial(N):
    if N<=0:
        #esto queda pendiente
        #aqui quiero generar una excepcion
        raise
        #pass
    if (N<=1):
        print('return 1')
        return 1
    else:
        print('return {} Factorial ({}-1)'.format(N,N))
        return N * Factorial(N-1)

n= input("desea calcular el factorial de (entre un numero):")
try:
    n= int(n)
    r= Factorial(n)
    print("El factorial de:",n," es ",r)
except TypeError:
    print('Entre un numero valido')
except ValueError:
    print('Entre un numero valido')
except:
    print('No se permiten valores menores a 0')
    
