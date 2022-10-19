conversion = '0123456789ABCDEF'

def cambio(n):
    if(n<=0):
        return ''
    else:
        remainder = n%16
        a = n//16
        return  cambio(a)+conversion[remainder]
        
print(cambio(65029))


