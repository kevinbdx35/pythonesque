# Les méthodes de classes

class Dog():
    nb_dogs = 0

    # Pour créer des propriétés qui sont partagées 
    # par toutes les instances de la même classe, il nous
    # faut les délcarer en dehors de notre constructeur

    def __init__(self, name, breed, age) -> None:
        self.name = name
        self.breed = breed
        self.age = age

    # Pour accéder à la propriété de classe, il nous faut utiliser la syntaxe nom_classe.nom_propriété
        Dog.nb_dogs += 1

    # Pour créer une méthode de classe, il nous faut utiliser le décorateur @classmethod
    #
    # Elles ne peuvent pas, contrairement aux méthodes classiques, accéder aux propriétés 
    # d'instance. Elles peuvent cependant accéder aux propriétés de classe, de par 
    # l'utilisation du mot-clé 'cls'
    @classmethod
    def aboyer(cls, text):
        print(f'The dog says : {text} - {cls.nb_dogs}')

    # Pour créer une méthode statique, nous devons utiliser le décorateur @staticmethod
    #
    # A contrario des méthodes de classe, les méthodes statiques n'ont pas accès par défaut
    # aux propriétés de classe. Elles ont un but principal de permettre le regroupement
    # de fonctionnalités sous un même nom de classe.
    @staticmethod
    def test_static():
        print('La méthode statique')

# Nous déclarons ici une autre classe avec une méthode statique
class Calcul():
    @staticmethod
    def addition(a, b):
        return a + b

# Nous mettons en place nos instances de la classe Dog
my_dog = Dog('Bernie', 'Labrador', 7)
my_dog_a = Dog('Rex', 'Doberman', 4)

print('Age du chien', my_dog.name, my_dog.age)

# Pour accéder à la propriété de classe, il nous faut
# utiliser la syntaxe nom_class.nom_prop
print(Dog.nb_dogs)

# Pour déclencher une méthode de classe
# nous utilisons la syntaxe nom_classe.nom_method()
Dog.aboyer('Wouaf Wouaf !!!')

# Pour déclencher une méthode statique
# nous utilison encore une fois la notation
# nom_classe.nom_method()
Dog.test_static()

print(Calcul.addition(1, 5))
