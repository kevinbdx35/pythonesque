#concatener des stings avec des integers
#il n est pas possible de concatener les deux
#il faut donc faire une conversion de type
num_char = len(input("What is you name?"))

#verification du type
print(type(num_char))

#nous devons convertir les integers en strings 
#pour pouvoir faire l'operation de concatenation
#l operation de concatenation ne fonctionne qu avec des strings
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))
