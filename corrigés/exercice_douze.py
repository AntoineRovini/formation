from builtins import open

file = open("fichier_a_lire.txt", 'r')
content = file.read()
print(content)
file.close()
