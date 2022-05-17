def SegundaParte():
    file='./Ejercicios/Ficheros/Data_ejercicios04.txt'
    fichero=None
    try:
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        fichero.close()
    except:
        pass
    finally:
        if fichero!=None: #Ha sido usado???
            fichero.close()




if __name__=="__main__":
    SegundaParte()

