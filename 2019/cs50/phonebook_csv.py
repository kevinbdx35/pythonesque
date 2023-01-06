# Saves names and numbers to a CSV file
import csv #importation du packet CSV
from cs50 import get_string

# Open CSV file
file = open("phonebook.csv", "a")

# Get name and number
name = get_string("Name: ")
number = get_string("Number: ")

# Print to file
writer = csv.writer(file) #déclaration de variable
writer.writerow((name, number))#writerow est une fonction de la bibliothèque CSV

# Close file
file.close()
