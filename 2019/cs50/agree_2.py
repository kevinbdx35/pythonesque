from cs50 import get_string

s = get_string("Do you agree?\n")

if s.lower() in ["yes", "y"]:
		print("Agree.")
elif s.lower() in ["no", "n"]:
		print("Not agree.");
