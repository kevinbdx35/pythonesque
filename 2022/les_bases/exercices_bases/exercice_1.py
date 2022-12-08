# Exercice 1

# Variables, elles sont entrées de manière dynamique
last_name = input('Quel est ton nom de famille : ')
first_name = input('Quel est ton prénom : ')

# Affichage ancienne méthode
print('Bonjour Monsieur ou Madame', first_name, last_name)

# Affichage nouvelle méthode f-string
print(f'Bonjour Monsieur ou Madame {first_name} {last_name}')