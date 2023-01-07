#input("A prompt for user")
input("what is your name?")

#nous mettons ici le résultat de la question dans une variable "name"
name = input("what is your name?")
#on imprime hello +  la réponse a la question precedente
print(f"hello {name}")

#il est possible d'inclure la fonction input dans la fonction print 
print("Hello " + input("What is your name?"))

#exercice : connaitre le nombre de lettre dans la chaine de caractere
#methode 1
nbre = len(input("What is your name?"))
print(nbre)
#methode 2
print(len(input("What is your name?")))
