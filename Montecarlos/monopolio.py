import random as rnd
m = [1500,1500,1500,1500]
while True:
  for i in range(0, len(m)):
    d1, d2  = rnd.randint(1, 6), rnd.randint(1, 6)
    print('jugador', i+1, 'dado 1', d1, 'dado 2',d2)
    s = d1+d2
    if(s == 4 or s == 10 or s == 14):
      m[i]-=100
      p = rnd.randint(0,len(m)-1)
      if(p!=i):
        m[p]+=100
      elif(p==i):
        p = rnd.randint(0,len(m)-1)
        if(p!=i):
          m[p]+=100
          
  if(0 in m):
    ju = m.index(0)
    max = max(m)
    gmax = m.index(max)
    print("el jugador ", ju+1,"perdio")
    print("el jugador ",gmax+1,"gano con $",max)
    break
 
print(m)