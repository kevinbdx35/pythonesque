# Les héritages

class Canid():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

# Si nous souhaitons protéger nos variables d'un accès extérieur
# il est possible de les prefixer d'un double underscore
# ce mécanisme permet grâce au Name Mangling
# d'empêcher l'accès à la variable à l'extérieur de la classe
        self.__hey = True
        self._protected = 25

# Si nous voulons rendre la variable accessible de façon contrôlée
# nous devons utiliser des getters et des setters
    @property
    def hey(self):
        return self.__hey

    @hey.setter
    def hey(self, value):
        self.__hey = value

    def make_sound(self):
        print('Canid makes sound !')

# Si nous voyons que nous avons des attributs / méthodes en commun entre plusieurs classes
# il n'y a pas besoin de les ré-écrire, 
# il suffit d'hériter de la classe pour les récupérer automatiquement
class Dog(Canid):
    def __init__(self, name, age, breed) -> None:
        #
        # Pour tout de même déclencher le constructeur de la classe parent, nous devons appeler
        # sa méthode __init__() en lui passant en paramètre les paramètres requis
        super(Dog, self).__init__(name, age)

        # 
        # Après que cela soit fait, il nous est possible de créer des attributs spécifiques
        # à notre classe enfant, via la syntaxe classique self.nom_attr = valeur
        self.breed = breed

    # Nous pouvons surcharger une méthode qui était présente
    # dans la classe parent en réécrivant son corps
    def make_sound(self):
        # super().make_sound() si l'on veut avoir aussi le fonctionnement de base
        print('Dog says : woaf !')

    # Pour modifier l'affichage de notre objet lorsque nous voulons le passer en paramètre
    # à la fonction print(), ou en avoir une représentation sous la forme d'un string,
    # il faut surcharger la méthode __str__()
    def __str__(self) -> str:
        return f"{self.name} est un chien de race {self.breed} et il a {self.age} ans"

my_canid = Canid('ABC', 25)
my_dog = Dog('Bernie', 17, 'Labrador')

my_animal = [my_canid, my_dog]

my_canid.make_sound()
my_dog.make_sound()

# L'accès à cette propriété passera forcément
# par le getter de part l'utilisation de Name Mangling
print(my_dog.hey)

# Une variable utilisant le Name Mangling du protected n'est pas
# réellement protégée de l'accès extérieur
print(my_dog._protected)

print(my_dog.breed)

print(my_dog)

#== LE POLYMORPHISME ==
# C'est une capacité de rassembler sous un même
# ensemble des sous ensembles héritant du type de l'ensemble
#
# De plus, le polymorphisme est la capacité dans un sous ensemble de faire
# appel à une surcharge de la méthode du parent
# 
# Dans un cadre d'une itération, on a donc la version la plus spécifique de la méthode
# et non à chaque fois celle du type de l'ensemble qui est déclenchée
for el in my_animal:
    el.make_sound()


#== HERITAGE MULTIPLE ==
class Person():
    def __init__(self, name) -> None:
        self.name = name

class WorkerJobs():
    def __init__(self, job) -> None:
        self.job = job

# Dans le cas d'un héritage multiple
# il va falloir mettre les deux classes
# séparée d'une virgule, entre les parenthèses de l'héritage
class Works(Person, WorkerJobs):
    def __init__(self, name, job) -> None:
        #
        # Il faut spécifier à quel construteur nous faisons appel
        # dans le constructeur de la classe enfant
        #
        # Ainsi, nous sommes sûr que les attributs seront settés 
        # correctement à l'instanciation
        Person.__init__(self, name)
        WorkerJobs.__init__(self, job)

my_worker = Works('John Smith', 'IT Manager')
print(my_worker.job)

