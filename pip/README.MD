# Installer pip sur Windows

Tout d'abord, téléchargez le script d'installation de pip en cliquant sur ce lien :
https://bootstrap.pypa.io/get-pip.py.

Ouvrez l'invite de commande Windows. Pour cela, appuyez sur la touche Windows + R, tapez "cmd" et appuyez sur Entrée.

Naviguez jusqu'au dossier où vous avez téléchargé le script d'installation de pip en utilisant la commande cd (change
directory). Par exemple, si vous avez téléchargé le script dans le dossier "Downloads", entrez la commande suivante :

````bash
cd Downloads
````

Entrez la commande suivante pour exécuter le script d'installation de pip :

````bash
python get-pip.py
````

Le script d'installation téléchargera et installera automatiquement pip. Une fois l'installation terminée, vous pouvez
vérifier que pip est installé en entrant la commande suivante :

````bash
pip --version
````

# Utiliser pip sur Windows

Maintenant que pip est installé sur votre système Windows, voici quelques commandes de base que vous pouvez utiliser
pour installer, mettre à jour et désinstaller des packages Python.

### Installer un package

Pour installer un package Python, ouvrez l'invite de commande Windows et entrez la commande suivante :

````bash
pip install <nom-du-package>
````

Remplacez <nom-du-package> par le nom du package que vous souhaitez installer. Par exemple, si vous souhaitez installer
le package "numpy", entrez la commande suivante :

````bash
pip install numpy
````

### Mettre à jour un package

Pour mettre à jour un package Python déjà installé sur votre système, entrez la commande suivante :

````bash
pip install --upgrade <nom-du-package>
````

Remplacez <nom-du-package> par le nom du package que vous souhaitez mettre à jour. Par exemple, si vous souhaitez mettre
à jour le package "numpy", entrez la commande suivante :

````bash
pip install --upgrade numpy
````

### Désinstaller un package

Pour désinstaller un package Python, entrez la commande suivante :

````bash
pip uninstall <nom-du-package>
````
Remplacez <nom-du-package> par le nom du package que vous souhaitez désinstaller. Par exemple, si vous souhaitez
désinstaller le package "numpy", entrez la commande suivante :

````bash
pip uninstall numpy
````

### Afficher une liste des packages installés

Pour afficher une liste des packages Python installés sur votre système, entrez la commande suivante :

````bash
pip list
````

### Rechercher un package

Pour rechercher un package Python sur PyPI, entrez la commande suivante :

````bash
pip search <nom-du-package>
````
Remplacez <nom-du-package> par le nom du package que vous souhaitez rechercher. Par exemple, si vous souhaitez
rechercher le package "numpy", entrez la commande suivante :

````bash
pip search numpy
````
### Conclusion

pip est un outil très utile pour les développeurs Python sur Windows, car il permet d'installer et de gérer facilement
des packages Python. Avec ce tutoriel, vous devriez être en mesure d'installer pip sur votre système Windows et de
l'utiliser pour installer et gérer des packages Python.