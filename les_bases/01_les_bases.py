# Les bases
from cmath import pi


print("Hello World !")
print('Hello World !')

# Ceci est un texte String
my_text = "Ceci est un texte que je mets dans une variable qui s'appelle my_text"
my_text_2 = 'Ceci est un autre texte que je mets dans une variable'
my_text_3 = """Bonjour, 
je peux écrire sur 
plusieurs lignes.
Utilisé pour la 
documentations.
"""

# Une vraible vide
my_variable = None

# Ceci est un nombre Integer
my_number = 32

# Ceci est un nombre à virgule Float
my_number_float = 3.14

# On peut ré-assigner une variable
my_text = 25

# J'affiche plusieurs variables
print(my_text, my_number, my_number_float)
print(my_text_3)

# Récupération d'une entrée utilisateur
# Un input est toujours un string, pour changer sa nature il faut le caster
input_user = input('Veuillez entrer un nombre : ')

# Casting des variables vers une autre type
input_number = int(input_user)
input_user_2 =  int(input('Veuillez entrer un deuxième nombre : '))
print(input_user)
print(type(input_user))
print(input_user_2)
print(type(input_user_2))

# Ajout de variable dans les chaînes de caratères
mon_genre = 'homme'
mon_age = 21
ma_chaine_formatee = "Je suis un {0} et j'ai {1} ans !".format(mon_genre, mon_age)
ma_chaine_formatee_2 = f"Je suis un {mon_genre} et j'ai {mon_age} ans !"
ma_chaine_formatee_3 = "Ma Moyenne est de {0:.2f} / 20".format(14.5)
ma_chaine_formatee_4 = f"Ma Moyenne est de {14.5:.2f} / 20"

# Permet de garantir une largeur dédiée ici de 2 caractères complétés par des zéros
ma_chaine_formatee_5 = f"Je possède {5:02} chiens"
# Permet de garantir une largeur dédiée ici de 10 caractères complétés par des zéros
ma_chaine_formatee_6 = f"Je possède {5:010.2f}"

# Affichage de nos chaînes formatées
print(ma_chaine_formatee)
print(ma_chaine_formatee_2)
print(ma_chaine_formatee_3)
print(ma_chaine_formatee_4)
print(ma_chaine_formatee_5)
print(ma_chaine_formatee_6)

# Rognage de mot
pierre ='Pierre'
mon_string = f"Je suis {pierre:.3s}"
print(mon_string)

