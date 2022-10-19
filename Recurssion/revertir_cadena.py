def atras(texto,n):
    global a
    if n ==0:
        a = a + texto[n]
        return a
    else:
        a = a + texto[n]
        return atras(texto,n-1)  
     

texto=input("texto : ")
a = ''

print (atras(texto,len(texto)-1))
