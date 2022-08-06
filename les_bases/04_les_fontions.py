# Les Fonctions

#== DECLARATION DE FONCTION ET SON APPEL ==
# Nous définissons une fonction par def nom(params)
def my_function(number = 5):
    for _ in range(0, number):
        print('Hello World')

# Pour que la fonction se lance il faut l'appeler
my_function()
print(' ')
my_function(2)

#== DECLARATION DE FONCTION AVEC RETOUR ET SON APPEL ==
# Une autre fonction qui nous donne ici un retour, 
# il faut savoir que tout fonction donne un retour 
# mais nous ne sommes pas obliger de le préciser 
# si ce n'est pas nécessaire
def addition(a, b):
    return a + b 

# Appelons la fonction addition et passons y 
# nos paramètres / arguments, ici 1 et 2 pour a et b
addition(1, 2)

#== DECLARATION D'UNE AUTRE FONCTION 
# Elle fait appel à une variable comme paramètre / argument d'entrée
# Nous pouvons aussi ici la portée d'une varible, passage par scope ou par valeur
number_a = 5

def increment(a):
    global number_a
    number_a += 1
    print('Dans la fonction, A vaut', number_a)

print('Avant la fonction A vaut : ', number_a)
increment(2)

#== EXTRA ==
# Méthode pythonique
print(f"Hello " * 5)