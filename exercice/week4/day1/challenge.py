######challenge day 1#########
a=input("entrer une chaine:"" ")
if(len(a)<10):
    print("chaîne pas assez longue")
elif(len(a)==10):
    print("chaîne de taille normale")
else:
    print("chaîne trop longue")
l=len(a)
print("La première lettre de votre chaine est:"" ",a[0])
print("La dernière lettre de votre chaine est:"" ",a[l-1])

t=""
for i in a:
    t=t+i
    print(t)

print("************** 4 Bonus ***************")
from random import shuffle
# t = x
b = []
for j in x:
    b.append(j)
shuffle(b)
c = ""
for z in b:
    c = c + z
print(c)