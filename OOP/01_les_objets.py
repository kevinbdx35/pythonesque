# Les objets

#== CREATION ==
# Pour créer un objet, nous devons passer par la création d'une classe
# nous devons pour cela utiliser le mot-clé 'class'
# le nom d'une classe commence toujours par une majuscule

class Dog():
    # Pour créer un objet à partir de notre classe, il faudra passer par
    # son constructeur qui est défini par la méthode __init__(self):
    # en passant des paramètres à cette méthode, on peut les placer dans notre objet
    def __init__(self, name, breed, age) -> None:
        
        # Nous créeons la propriété d'instance self.nom_propriété aussi appelé attribut et on lui donne une valeur
        # par l'affectation des paramètres du constructeur
        self.name = name
        self.breed = breed
        self. age = age
        self.blabla = True

#== GETTER ==
# Le getter permet de voir / affiche une propriété personnalisée en plus de notre classe
# la propriété en plus aussi appelée attribut est créer par le setter

# Création d'un getter avec la syntaxe moderne
    @property
    def color(self):
        return 'Blue'

# Création d'un getter avec l'ancienne syntaxe
# Pour créer un getter (des noms de propriétés personnalisés)
# qui permet d'avoir un contrôle sur la syntaxe ou le type de propriétés
    def __getattr__(self, item):
        if item == "age_str":
            return f"{self.age} ans"
        raise AttributeError(item)
    
    @property
    def double_age(self):
        return self.age * 2

#== SETTER ==
# Le setter permet de créer de nouveaux attributs / propriétés personnalisé(e)s

# Création d'un setter avec la syntaxe moderne
# Il faut avoir le getter @property pour avoir le sette sinon ça ne fonctionnera pas
    @double_age.setter
    def double_age(self, value):
        self.age = int(value / 2)

# Pour créer une setter avec l'ancienne syntaxe
# un setter (des contôles potentiels sur nos affectations de variables)
# on se sert de la surcharge de ma méthode dunder __setattr__()
    def __setattr__(self, key, value) -> None:
        if key == 'human_age':
            self.age = int(value / 7)
        else:
            super().__setattr__(key, value) # Il ne faut pas oublier ceci sous peine de ne plus pouvoir setter de propriétes

#== METHODES ==
# Un objet vient toujours (en tout cas le plus souvent)
# avec ses attributes / propriétés (noms, paramètres) et ses methodes (verbes, action)
# Pour faire une méthode, il nous faut faire une fonction dans notre classe
# qui possède comme premier paramètre le mot-clé 'self' (ce qui l'attachera à notre instance)
#
# Via ce mot clé, il nous est également possible d'accéder 
# à toutes les propriétés et méthodes de notre instance
    def aboyer(self, text):
        print(f'{self.name} says : {text}')

#== INSTANCE ==
# pour créer une instance de notre classe Dog, 
# il nous faut faire appel au constructeur mon_class(params)
# qui va nous renvoyer une variable du type de la classe
my_dog = Dog('Bernie', 'Labrador', 7)
# Affichage de l'objet
print(my_dog)

#== ACCES ==
# Pour accéder aux prorpiétés de l'objet
# on se sert de la notation mon_instance.nom_prop
print(my_dog.age)

my_dog.age = 21
print(my_dog.age)

my_dog.human_age = 21
print(my_dog.age)

print(my_dog.color)
