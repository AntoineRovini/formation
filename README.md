# Partie 1 : Formation simple Python

### Axe un : syntaxe de Python

Python est un langage de programmation de haut niveau, interprété et multiplateforme,
qui est largement utilisé pour la science des données, l'apprentissage automatique,
le développement web et bien plus encore.
Voici une présentation rapide de la syntaxe de base de Python.

### Axe deux : les variables

Les variables sont utilisées pour stocker des valeurs dans un programme. 
En Python, vous pouvez déclarer une variable en assignant une valeur à un nom. Par exemple :

```
x = 5
y = "Hello, world!"
```

Dans cet exemple, x est une variable qui stocke la valeur entière 5,
et y est une variable qui stocke la chaîne de caractères "Hello, world!".


### Axe trois : les opérateurs

Les opérateurs sont utilisés pour effectuer des opérations sur des variables. Voici quelques-uns des opérateurs les plus
couramment utilisés en Python :
````
+:addition
-: soustraction
*: multiplication
/ : division
// : division entière
% : modulo (reste de la division entière)
** : exposant
````

Voici un exemple d'utilisation d'opérateurs :
````
a = 10
b = 3
c = a + b     # addition
d = a - b     # soustraction
e = a * b     # multiplication
f = a / b     # division
g = a // b    # division entière
h = a % b     # modulo
i = a ** b    # exposant
````

### Axe quatre : les fonctions

Les fonctions sont des blocs de code qui effectuent une tâche spécifique.
En Python, vous pouvez définir une fonction en utilisant le mot-clé def.
Voici un exemple de définition de fonction :
````
def addition(a, b):
    c = a + b
    return c
````

Dans cet exemple, nous avons défini une fonction simple addition qui prend deux arguments a et b et renvoie leur somme.
Il est possble de créer des fonctions plus complexes, que nous verrons plus tard.

### Axe cinq : les structures de contrôle

Les structures de contrôle sont utilisées pour contrôler le flux d'exécution d'un programme.
Voici quelques-unes des structures de contrôle les plus couramment utilisées en Python :

````
if : exécute un bloc de code si une condition est vraie
else : exécute un bloc de code si la condition de if est fausse
elif : exécute un bloc de code si une autre condition est vraie
while : exécute un bloc de code tant qu'une condition est vraie
for : exécute un bloc de code pour chaque élément d'une liste ou d'un itérateur
````
Voici un exemple d'utilisation de la structure de contrôle if :

````
x = 5
if x > 0:
    print("x est positif")
elif x == 0:
    print("x est nul")
else:
    print("x est négatif")
    
````

Dans cet exemple, nous avons utilisé la structure de contrôle if pour afficher un message différent selon que la
variable x est positive ou négative.


# Partie 2 : Exercices de calculs en Python


### Exercice 1 : Conversion de température

Écrivez un programme Python qui demande à l'utilisateur d'entrer une température en degrés Celsius,
puis convertit cette température en degrés Fahrenheit et affiche le résultat.

La formule de conversion est la suivante :
``
F = (C * 9/5) + 32
``

### Exercice 2 : Calcul de l'aire d'un cercle

Écrivez un programme Python qui demande à l'utilisateur de saisir le rayon d'un cercle,
puis calcule et affiche l'aire de ce cercle.

La formule pour calculer l'aire d'un cercle est la suivante :
``
A = pi * r^2
``

où pi est une constante mathématique qui représente la valeur de pi (environ 3,14) et r est le rayon du cercle.

### Exercice 3 : Calcul de la moyenne

Écrivez un programme Python qui demande à l'utilisateur de saisir trois nombres,
puis calcule et affiche leur moyenne.

### Exercice 4 : Vérification de parité

Écrivez un programme Python qui demande à l'utilisateur de saisir un entier,
puis vérifie si cet entier est pair ou impair et affiche le résultat.

### Exercice 5 : Calcul de la somme des entiers
Écrivez un programme Python qui demande à l'utilisateur de saisir un entier, puis calcule la somme de tous les entiers
de 1 à cet entier et affiche le résultat.

### Exercice 6 : Calcul de la moyenne

Écrivez un programme Python qui prend une liste de nombres en entrée et calcule leur moyenne.

### Exercice 7 : Vérification de la validité d'un mot de passe

Écrivez un programme Python qui demande à l'utilisateur de saisir un mot de passe et vérifie s'il est valide.
Un mot de passe est considéré comme valide s'il remplit les conditions suivantes :
- Avoir une longueur minimale de 8 caractères,
- Contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial (par exemple, !,
@, #, $)
- Pour vous aider, voici la ligne qui va définir la validité du mot de passe :
``pattern = “^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$”``


### Exercice 8 : Jeu de devinette de nombre

Écrivez un programme Python qui génère un nombre aléatoire entre 1 et 100 et demande à l'utilisateur de deviner le
nombre.
Si l'utilisateur devine correctement, le programme affiche "Bravo !" et s'arrête.
Sinon, le programme donne un indice (plus grand ou plus petit) et demande à l'utilisateur de deviner à nouveau jusqu'à
ce qu'il trouve le bon nombre.

### Exercice 9 : Jeu de devinette de mot
Écrivez un programme Python qui choisit un mot aléatoire dans une liste prédéfinie et demande à l'utilisateur de deviner
le mot.
Si l'utilisateur devine correctement, le programme affiche "Bravo !" et s'arrête. Sinon, le programme donne un indice
(par exemple, la première lettre) et demande à l'utilisateur de deviner à nouveau jusqu'à ce qu'il trouve le bon mot.
Voici un exemple de code pour vous aider à démarrer :

### Exercice 10 : Création d'un gestionnaire de tâches
Écrivez un programme Python qui permet à l'utilisateur de créer une liste de tâches et de les gérer.
Le programme doit permettre à l'utilisateur de :
- Ajouter une tâche
- Afficher toutes les tâches
- Supprimer une tâche
- Marquer une tâche comme terminée

### Exercice 11 : Le fermier
Cet exercice est plus complexe que les précédents et utilise les connaissances théoriques acquises ainsi
que de bonnes connaissances en mathématique. Il se peut que vous deviez utiliser l'algorithme de Gauss, des matrices ou
tout algorithme qui pourrait vous être utile à résoudre le problème le plus efficacement possible.

Un agriculteur cultive des céréales : de l'avoine, du blé, du maïs, de l'orge et du soja.
Il utilise quatre types différents d'engrais (F1, F2, F3 et F4),
dans les quantités suivantes (par tonne d'engrais pour produire une unité de céréales) :

|        | F1  | F2  | F3  | F4  |
|--------|-----|-----|-----|-----|
| avoine | 1   | 1   | 2   | 0   |
| blé    | 0   | 2   | 1   | 0   |
| maïs   | 1   | 0   | 0   | 3   |
| orge   | 0   | 1   | 1   | 1   |
| soja   | 2   | 0   | 0   | 2   |

En gardant à l'esprit qu'il dispose de quantités limitées d'engrais chaque année,
l'agriculteur aimerait optimiser sa production en fonction des prix des céréales.
Vous allez donc développer un programme qui prendra en paramètre les ressources en engrais et les prix de chaque type de
céréale. Le programme affichera les quantités à produire, ainsi que la valeur totale de sa production.
La sortie devrait ressember à ça :

![img.png](img/img.png)

### Exercice 12 : Ouvrir et lire un fichier texte

Ecrivez un programme Python qui est capable d'ouvrir puis lire des mots et calcule le nombre de caractères de chaque
mot. Le programme doit ensuite afficher le contenu du fichier.

Conseil : documentez vous sur open() et read().


Ces exercices devraient vous aider à vous familiariser avec la syntaxe de base de Python et à commencer à coder en
Python.
Les corrigés figurent dans le dossier ```corrigés/```, d'autres exercices et une suite sera rajoutée au fur et à mesure
du temps.
Essayez de comprendre ce que veut dire chaque chose pour ne pas être perdu !

# Sources
````
documentaion Python :
https://www.python.org/
https://www.python.org/doc/
Documentation pip (packet manager)
https://pypi.org/project/pip/
PyCharm Community :
https://www.jetbrains.com/edu-products/download/other-PCE.html
installation Git:
https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git
````