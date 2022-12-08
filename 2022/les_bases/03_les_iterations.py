# Les Structures Itératives

my_iterator = 0

#== BOUCLE WHILE ==
# Phase comparaison et entrée dans la boucle
while my_iterator < 10:
    # Phase de modification de la variable d'itération
    my_iterator += 1

    # Phase d'instructions
    if my_iterator == 3:
        continue            # Nous passons directement à l'itération suivante
    if my_iterator % 5 == 0:
        break               # Nous stoppons la boucle
    if my_iterator % 2 == 0:
        print('Bonjour')
    pass                    # Nous passons sans rien faire


#== BOUCLE FOR ==
# range(début, fin, pas)
for my_var in range(0, 10, 2):
    print('La variable vaut : ', my_var)