#nous mettons ici le résultat de la question dans une variable "name"
name = input("what is your name?")
#on imprime hello +  la réponse a la question precedente
print(f"hello {name}")

name = "Jack"
print(name)

name = "Rodrigo"
print(name)

name = "Kevin"
print(name)

#meilleure pratique pour nommer une variable
#en Python nous utilisons par convention SNAKE_CASE,
#un underscore entre chaque mot
user_name = input("what is your name?")
lenght = len(user_name)
print(lenght)

#exercice : 
# echanger deux variables, 
# pour cela on passe par une variable temporaire tmp
a = input("a : ")
b = input("b : ")

tmp = a
a = b
b = tmp

print("a = " + a)
print("b = " + b)
