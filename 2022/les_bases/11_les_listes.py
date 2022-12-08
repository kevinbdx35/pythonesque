# Les listes

#== DECLARATION ==
# Déclaration d'une liste avec les []
# Une liste peut contenir tout type de donnée
from re import M


my_variable = [1, 2, 3, "Bonjour", True, [4, 5, 6]]
# Nous pouvons afficher l'ensemble de la liste
print(my_variable)
# Nous pouvons afficher un élement en particulier en faisant appel à son index
print(my_variable[3])
print(my_variable[5])
# Si la liste contient une autre liste, 
# nous faisons spécifie l'index de la premier liste 
# puis celui de la deuxieme liste de l'élement que nous voulons obtenir
print(my_variable[5][1])

#== TRIER UNE LISTE ==
my_numbers = [4, 1, 5, 2, 3]
# Pour trier une liste, nous utilisons la méthode .sort(), tri en mode croissant
my_numbers.sort()
print(my_numbers)

# Pour trier en mode décroissant
my_numbers.sort(reverse=True)
print(my_numbers)

# Nous pouvons choisir d'afficher une version 
# triée uniquement pour l'affichage
print(sorted(my_numbers))

#== AJOUTER UN ELEMENT ==
# Pour ajouter un élément à une liste, 
# nous utilisons la méthode .append()
# ajoute à la fin de la liste
my_numbers.append(90)
print(my_numbers)

# Pour ajouter une élément à index en particulier
# nous utilisons la méthode .insert(index, valeur) 
my_numbers.insert(2, 100)
print(my_numbers)

# Pour ajouter le contenu d'une liste à une autre liste
# nous utilisons la méthide .extend()
# ajoute à la fin de la liste
my_numbers.extend([8, 7])
print(my_numbers)

#== RETIRER UN ELEMENT ==
# Pour retirer une élément à partir d'un index
# nous utilisons la méthode .pop(index)
my_numbers.pop(2)
print(my_numbers)

# Pour retirer un élément de la liste par rapport à son contenu
# nous utilions la méthode .remove(valeur)
my_numbers.remove(90)
print(my_numbers)

#== AFFICHAGE ==
# Pour itérer puis afficher le contenu
# de la liste, nous pouvons utiliser la boucle for
for i in my_numbers:
    print(i)

#== LIST COMPREHENSION ==
# Nous générons ici une liste
# Nous obtenons une liste de nombres allant de 1 à 10 compris
list_a = [x for x in range(1, 11)]
print(list_a)

# Il est possible d'altérer l'entrée
# de l'itérateur en modifiant l'expression
# à gauche et la list comprehension
list_b = [x ** 2 for x in range(1, 11)]
print(list_b)

# Via cette syntaxe, nous pouvons avoir 
# l'équivalent d'un .map() dans d'autre langage
list_c = [x ** 2 for x in list_a]
print(list_c)

# Il est aussi possible de filtrer les valeurs
list_d = [x for x in range(1, 11) if x % 2 == 0]
print(list_d)

# Il est également possible de conditionner l'affectation de variable
list_e = ['EVEN' if x % 2 == 0 else '0DD' for x in list_a]
print(list_e)