#operateurs mathématiques
a = 3 + 4
b = 7 - 3
c = 4 * 5

#la division en Python va toujours generer un type float
d = 8 / 4

#permet d avoir acces aux exposants ou nombre a la puissance
e = 2 ** 2

print(f"{a}, {b}, {c}, {d}, {e}")

#si vous faites plusieurs calculs sur la même ligne
#il faudra respecter les regles de priorites des 
#mathematiques classiques, voici un moyen mnemotechnique :

#PEMDAS
#Parentheses ()
#Exposants **
#Multiplication *  et Division / (meme niveau de priorite)
#Addition + et Substraction - (meme niveau de priorite)

#pour les operateurs qui sont au meme niveau de priorite
#le calcul qui se trouve le plus a gauche est celui qui sera prioritaire

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
