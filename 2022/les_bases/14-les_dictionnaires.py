# Les dictionnaires

#== CREATION ==
# Dictionnaire vierge
my_dict = {}

# Dictionnaire avec système de clé : valeur
# il ne faut jamais avoir de doublons de clé
my_dict_a = {'test':'texte de test', 1:25, 'test_a': True}
print(my_dict_a)

#== ACCEDER A UN VALEUR ==
# Pour accéder à la valeur liée à la clé d'un dictionnaire
# nous utilisons la syntaxe ci-dessous
print(my_dict_a[1])
print(my_dict_a['test'])

#== AJOUTER UN ELEMENT ==
# Nous créons une clé et nous lui donnons une valeur
# Ajoute la paire clé:valeur à la fin du dictionnaire
my_dict_a['Coucou'] = 'Texte lié à la clé Coucou'
print(my_dict_a)

#== MODIFICATION DE VALEUR ==
# Modification de valeur d'une clé
my_dict_a['Coucou'] = 247
print(my_dict_a)

#== AFFICHAGE ==
# Afficher uniquement les clés de notre dictionnaire
print(my_dict_a.keys())
# En faisaint une itération
for k in my_dict_a.keys():
    print(k)

# Afficher uniquement les valeurs de notre dictionnaire
print(my_dict_a.values())

# Pour obtenir à la fois les pairs clé:valeur de notre dictionnaire
# nous avons la méthode .items()
print(my_dict_a.items())
# En faisaint une itération
for key, value in my_dict_a.items():
    print(f"key : {key} - value : {value}")

#== SUPPRIMER UN ELEMENT ==
# Pour supprimer un élement du dictionnaire, nous utilisons del
# il faut que l'élément existe sinon nous aurons une erreur
del my_dict_a['Coucou']
print(my_dict_a)

# Il existe aussi la méthode .pop(clé)
# nous devons y renseigner la clé 
my_dict_a.pop('test')
print(my_dict_a)

#== FUSIONNER ==
# Pour fusionner deux dictionnaires ensemble
# nous avons la méthode .update()
my_dict_a.update({2:'Valeur de la clé 2'})
print(my_dict_a)

