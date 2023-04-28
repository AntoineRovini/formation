import re

password = input("Entrez votre mot de passe: ")
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(pattern, password):
    print("Le mot de passe est valide")
else:
    print("Le mot de passe n'est pas valide")
