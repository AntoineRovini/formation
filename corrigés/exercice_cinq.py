nombre = int(input("Entrez un entier : "))
somme = 0
for i in range(1, nombre+1):
    somme += i
print("La somme des entiers de 1 à", nombre, "est :", somme)