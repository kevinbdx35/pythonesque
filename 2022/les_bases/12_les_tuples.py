# Les tuples

# Déclaration de la fonction get_num_and_num_square() qui retourne un tuple
def get_num_and_num_square():
    """
    Cette fonction permet de retourner un nombre et son carrée
    """
    num = int(input('Veuillez entrer une nombre : '))

    # Ici, nous retournons un tuple / tuple packing pour rassembler dans un tuple plusieurs valeurs
    return num, num ** 2

# Nous appelons la fonction get_num_and_num_square() afin qu'elle s'exécute 
# et nous la mettons dans une variable que l'on affiche
my_result = get_num_and_num_square()
print(my_result)

# Nous pouvons aussi afficher séparément chaque élément du tuple, 
# il faut néanmoins bien respecter le même nombre d'élements de ce tuple
number, squared = get_num_and_num_square()
print(number)
print(squared)

# Déclaration d'un tuple avec la syntaxe entre parenthèses
my_tuple = (1, 2, 3, 4, 5)
# Déclaration d'un tuple, simplement en séparant les éléments par une virgule
my_tuple_2 = 1, 2, 3, 4, 5

# Déclaration de la fonction operation() qui retourne un tuple de 4, composé d'opération
def operation(a, b):
    return a + b, a - b, a * b, a / b

# Ici nous entrons les variables de manière dynaimque et nous affichons le résultat de chaque tuple
num_a = int(input('nombre a : '))
num_b = int(input('nombre b : '))
add, sub, mul, div = operation(num_a, num_b)
print("Addition : ", add)
print("Soustraction : ", sub)
print("Multiplication : ", mul)
print("Division : ", div)