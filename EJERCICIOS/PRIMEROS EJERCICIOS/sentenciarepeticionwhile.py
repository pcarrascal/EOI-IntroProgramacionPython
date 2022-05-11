print("Antes del while")
valor=0
while(valor<5):
    valor+=1
    if(valor>3):
        #continue
        break
    print(f"Valor actual:{valor}")
  
print("Despues del while")