
def conv(texto):
    texto = texto.replace(" ","").lower()
    return texto
  
def giro(texto, n):
  global a
  if n==0:
    a = a + texto[n]
    return a 
  else:
    
    a = a + texto[n]
    return giro(texto, n-1)
  
texto = input('ingrese cadena :')
texto = texto.replace(" ","").lower()
a = ''
print(giro(texto, len(texto)-1))

if texto==a:
  print("palindromo")
else:
  print("no es palindromo")