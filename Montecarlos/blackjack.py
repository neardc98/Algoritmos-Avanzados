import random
cartas=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
total1=[]
total2=[]
usu1=0
usu2=0
while(True):
    usu=input("desea una carta? ")
    if usu=="si":
        usu1=random.choice(cartas)
        if cartas=="A":
            valor=1
        elif cartas=="J" or cartas=="Q" or cartas=="K":
            valor=10
        print(usu1)
    total1.append(usu1)
    total1+=total1
    break
while(True):
    usu=input("desea una carta? ")
    if usu=="si":
        usu2=random.choice(cartas)
        if cartas=="A":
            valor=1
        elif cartas=="J" or cartas=="Q" or cartas=="K":
            valor=10
        print(usu2)
    total2.append(usu2)
    total2+=total2
    break
if total1==21:
    print("usuario 1 ganador")
elif total2==21:
    print("usuario 2 ganador")
else:
    print("perdieron")

