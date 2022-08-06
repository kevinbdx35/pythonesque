# Les sets

#== TRANSFORMER UNE LISTE EN SET ==
# Déclarations d'une liste
my_list = [1, 2, 2, 3 , 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# Affichage de la liste
print(my_list)

# Transformons cette liste en set.
# Le set permet de supprimer les doublons d'une liste 
# et peut dans certains cas faire un tri automatique d'ordre croissant sur les nombres
# mais il est préférable d'utiliser une fonctionnalité de tri qui sera beaucoup plus fiable
# si vous souhaitez faire de type d'opération
my_set = set(my_list)
# Affichage du set, nous pouvons voir que les doublons ont été supprimés
print(my_set)

#== CREER UN SET ==
# Nous pouvons également créer une set vierge en utilisant son constructeur
# Permet de créer un set vierge
my_set_2 = set()
# Affichage du set vierge
print(my_set_2)

# Nous pouvons créer une set remplit via cette syntaxe
my_set_3 = {1, 4, 6}
# Affichage du set remplit
print(my_set_3)

#== AJOUTER UN ELEMENT ==
# Pour ajouter une élément à un set, nous nous servons de la méthode .add()
my_set_2.add(3)
# Nous pouvons voir ici que nous avons bien ajouter le nombre 3 à notre set vierge -> my_set_2
print(my_set_2)

#== FUSIONNER DEUX SETS ==
# Pour fusionner deux sets ensemble, nous nous servons de la méthode .update()
my_set.update(my_set_2)
print(my_set)

#== RETIRER UN ELEMENT ==
# Pour retier une élément d'un set, il y a deux méthodes.
# Méthode .remove(), peut générer une erreur si la valeur n'est pas dans notre set, méthode plus rapide
my_set_2.remove(3)
# Méthode .discard, supprime et ne génère pas d'erreur si la valeur n'existe pas, méthode plus lente mais plus sécure
my_set_2.discard(25)

#== TEST ENTRE DEUX SETS ==
my_set_a = {1, 2, 3, 4, 5, 6}
my_set_b = {5, 6, 7, 8, 9, 10}

# Pour tester si nous avons présence ou absence d'élément en commun entre deux sets
print(my_set_a.isdisjoint(my_set_b))
print({25, 50, 99}.isdisjoint(my_set_b))

# Pour tester si un set fait partie ou non d'un autre set
print({1, 2, 3}.issubset({1, 2, 3, 4, 5, 6}))

# Pour tester si un set comprend un autre set
print({1, 2, 3, 4, 5, 6}.issuperset({1, 2, 3}))

#== DIAGRAM DE VERN ==
# Union
print(my_set_a.union(my_set_b))
# Intersection
print(my_set_a.intersection(my_set_b))
# Différence
print(my_set_a.difference(my_set_b))
# Différence
print(my_set_b.union(my_set_a))
# Différence symétrique (réunion moins intersection)
print(my_set_a.symmetric_difference(my_set_b))