#####################################Exercice1##############################
Créez un ensemble appelé my_fav_numbers avec tous vos numéros favoris.
my_fav_numbers= {16, 15, 17, 14, 18}
#Ajoutez deux nouveaux numéros à l'ensemble
my_fav_numbers.add(19)
print(my_fav_numbers)
#Supprimez le dernier numéro
my_fav_numbers.remove(15)
#Créez un ensemble appelé friend_fav_numbersavec les numéros favoris de votre ami
friend_fav_numbers={1,2,4,5}
#Concaténer my_fav_numberset friend_fav_numbers à une nouvelle variable appelée our_fav_numbers
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#####################################Exercice2##############################
# Question: Étant donné un tuple dont la valeur est un entier, est-il possible d'ajouter plus d'entiers au tuple ?
# Notre réponse: Les tuples sont immuables, ce qui signifie que nous ne pouvons pas modifier, ajouter ou supprimer des éléments après la création du tuple

######################################Exercice3#############################
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Supprimez "Banana" de la liste
basket.remove("Banana")
#Supprimez "Blueberries" de la liste
basket.remove( "Blueberries")
#Ajoutez "Kiwi" à la fin de la liste
basket.append( "Kiwi")
basket.append( "Apples")
#Ajoutez "apples" à la fin de la liste
basket.insert(0,"Apples")
print(basket)
#Comptez combien de apples il y a dans le panier
s=0
for i in range (0,4):
    if(basket[i]=="Apples"):
      s=s+1
      i=i+1
print(s)
#vider le pannier
basket.clear()
print(basket)

######################################Exercice4#############################
#Question: Qu'est-ce qu'un float? Quelle est la différence entre un entier et un flottant
#Réponse: un float est un nombre à virgule et un entier est un nombre à virgule
#Créez une liste contenant la séquence suivante 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# my_tuple = (1.5, 2, 2.5,3,3.5,4,3.5,5)
# print(my_tuple)

######################################Exercice5#############################
# Utilisez une forboucle pour imprimer tous les nombres de 1 à 20 inclus
for i in (1,20):
  print(i)
# En utilisant une forboucle, qui boucle de 1 à 20 (inclus), imprimez chaque élément qui a un index pair
for i in range(1,20):
  if i%2==0:
    print(i)


######################################Exercice6###########################
#Écrivez une boucle while qui demandera continuellement à l'utilisateur son nom, à moins que l'entrée ne soit égale à votre nom
nom="Tatiana"
a=input("entrer votre nom:"" ")
while(a!=nom):
  a=input("entrer votre nom:"" ")

######################################Exercice7###########################
o=input("entrer vos fruits préférés:"" ")
liste=o.split(" ")
p=input("entrer un de vos fruits préférés:"" ")
if p in liste :
  print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
else:
  print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")

######################################Exercice8###########################
garniture  =  "" 
serie  =  "" 
prix  =  0 ; 
while  garniture . lower ()  !=  "quitter"  : 
    garniture  =  input ( "Entrez une serie de garnitures de pizza" ) 
    if  garniture . lower ()  !=  "quitter"  : 
        print ( "Nous ajouterons cette garniture" ) 
        serie  +=  garniture  +  " " 
    prix  +=  12.5 

print ( serie , " Et le prix total est :" , prix )
