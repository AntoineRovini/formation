# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

pi=3.14

def exo1():
    C=float(input("temperature en °C : "))
    F=(C*9/5)+32
    print(F)
    return F

def exo2():
    R = float(input("rayon du cercle : "))
    A=pi*(R**2)
    print(A)
    return A

def exo3():
    nombres = [int(input("nombre1 : ")),int(input("nombre2 : ")),int(input("nombre3 : "))]
    moy = (nombres[0]+nombres[1]+nombres[2])/3
    print(moy)
    return moy

def exo4():
    nombre = int(input("nombre entier : "))
    reste = nombre%2
    if reste == 0 :
        parité = "pair"
    else:
        parité = "impair"
    print(parité)
    return parité

def exo5():
    nombre = int(input("nombre entier : "))
    tot=0
    while nombre>0:
        tot=tot+nombre
        nombre=nombre-1
    print(tot)
    return tot

def exo6():
    nombres = (input("nombres séparés par des virgules : "))
    n = [int(x) for x in nombres.split(",")]
    moy=sum(n)/len(n)
    print(moy)
    return moy

def exo7():
    mdp = (input("Nouveau Mot de Passe : "))
    if len(mdp)<8:
        print("8 caractères minimum")
    else:
        c=0
        valid = False
        while c<len(mdp) :
            if mdp[c] == "!" or mdp[c] == "@" or mdp[c] == "#" or mdp[c] == "$" :
                valid = True
            c=c+1

        if valid == False :
            print("au moins 1 caractère spécial par exemple, !, @, #, $")
        else :
            print ("mdp valide")

def exo8():
    import random
    A = random.randint(1, 100)
    B = int(input("trouvez le chiffre entre 1 et 100 : "))

    while A != B:
        if A < B :
            print("trop grand")
        if A > B:
            print("trop petit")
        B = int(input("trouvez le chiffre entre 1 et 100 : "))
    print("Bravo !")

def exo9():
    import random

    A = random.choice(seq=["un", "deux", "trois"])
    B = input("trouvez le bon mot : ")
    C = 0
    D = len(A)
    while C < D:
        if A == B :
            print("Bravo !")
            C=D
        if A != B:
            print("raté, voici un indice : ", A[C])
            B = input("trouvez le bon mot : ")
            C=C+1

def exo10():
    A = 0
    task = []
    taskc = []
    while A != 5:
        A = int(input("Bonsoir, appuyez sur 1 pour ajouter une tâche, 2 pour afficher toutes les tâches, 3 pour supprimer une tâche, 4 pour clôturer une tache, 5 pour quitter : "))
        match A:
            case 1 :
                task.append(input("nouvelle tâche : "))
            case 2 :
                print("tâches en cours : ", task)
                print("tâches clôturées : ", taskc)
            case 3:
                B = int(input("selectionnez une tache à supprimer : "))
                del task[B-1]
            case 4:
                B = int(input("selectionnez une tache à clôturer : "))
                print(task[B-1], "à été clôturée")
                taskc.append(task[B-1])
                del task[B - 1]
            case 5:
                print("au revoir")
            case _:
                print("erreur de saisie !")

def exo11() :
    """Acquisition des paramètres"""
    R = []
    C = []
    x=0
    while x != 4:
        nombres = input("Veuillez renseigner la valeur des engrais F1, F2, F3, F4 séparés par une virgule : ")
        x = len(nombres.split(","))
    R = [int(x) for x in nombres.split(",")]
    while x != 5:
        nombres = input("Veuillez renseigner le prix de vente des céréales avoine, blé, maïs, orge et soja séparés par une virgule : ")
        x = len(nombres.split(","))
    C = [int(x) for x in nombres.split(",")]

    R1 = R[0]
    R2 = R[1]
    R3 = R[2]
    R4 = R[3]

    C1 = C[0]
    C2 = C[1]
    C3 = C[2]
    C4 = C[3]
    C5 = C[4]

    """calcul"""
    P1 = min(R1, R2, R3 // 2)
    P2 = min(R2 // 2, R3)
    P3 = min(R1, R4 // 3)
    P4 = min(R2, R3, R4)
    P5 = min(R1 * 2, R4 * 2)

    Ptot = P1*C1+P2*C2+P3*C3+P4*C4+P5*C5

    print(f"ressources : {R1} F1, {R2} F2, {R3} F3, {R4} F4 \n")

    print(f"Oat: {P1} units at ${C1}/units")
    print(f"Wheat: {P2} units at ${C2}/units")
    print(f"Corn: {P3} units at ${C3}/units")
    print(f"Barley: {P4} units at ${C4}/units")
    print(f"Soy: {P5} units at ${C5}/units\n")

    print(f"Total production value: ${Ptot}")

def exo12() :
    #chemin = input("merci d'indiquer le chemin du fichier à ouvrir")
    fichier = input("merci d'indiquer le nom du fichier txt a ouvrir")
    fichier = fichier + ".txt"
    f = open(fichier)
    txt = f.read()
    i=0
    charac = []
    for x in txt.split():
        charac.append(len(str(x)))
        i=i+1
    mots = i
    print(f"\nle texte contient {mots} mots\n")
    print(f"la taille des mots est respectivement de : {charac}\n")
    print(txt)
#1964-002.txt

def exo13():
    fichier = input("merci d'indiquer le nom du fichier a créer (défaut: exercice_treize) : ")
    if len(fichier) == 0:
        fichier = "exercice_treize"
    fichier = fichier+".txt"

    txt = open(fichier, mode='w')
    txt.write(f"Hello world!\nexercice de la posterite!\nGoodbye World!")
    txt.close()

def exoTLE():
    """L'idée ici est d'ouvrir un fichier TLE,
    de reconnaitre s'il s'agit de paramètres en 2 ou 3 lignes
    d'en extraire les paramètres orbitaux de chaque satellite
    puis de créer un nouveau fichier txt avec ces paramètres Kepleriens"""

    fichier = input("merci d'indiquer le nom du fichier TLE (défaut: 1964-002) : ")
    if len(fichier) == 0:
        fichier = "1964-002"
    fichier = fichier+".txt"

    f = open(fichier, "r")
    lignes = f.readlines()
    nb_l = int(len(lignes))

    l1 =lignes[0].split()
    l2 =lignes[1].split()
    l3 =lignes[2].split()


    sat = []
    Epoch = []
    INC = []
    RAAN = []
    ECC = []
    AoP = []
    MA = []
    MM = []

    if nb_l%3==0:
        if l2[0]=="1" and l3[0]=="2":
            type=3
        else:
            type = 0

    elif nb_l%2==0:
        if l1[0]=="1" and l2[0]=="2":
            type=2
        else :
            type = 0
    else:
        type = 0

    match type:
        case 0:
            print("merci d'utiliser un format TLE/3LE standard")
            """
        case 2:
            print("format 2LE")
            for ligne in lignes:
                l=l+1
                if l%2==1:
                    sat[(l // 2)-1]="sat"+l//2
                    Epoch[(l // 2)-1]= "20"+ligne[6]+" "+ligne[7]
                else:
                    INC[(l // 2)-1] = ligne[2]
                    RAAN[(l // 2)-1] = ligne[3]
                    ECC[(l // 2)-1] = ligne[4]
                    AoP[(l // 2)-1] = ligne[5]
                    MA[(l // 2)-1] = ligne[6]
                    MM[(l // 2)-1] = ligne[7]
            """
        case 3:
            print("format 3LE")
            for l in range(nb_l):
                ligne = lignes[l].split()
                if (l)%3 == 0:
                    sat.append(ligne)
                if (l) % 3 == 1:
                    Epoch.append("20" + ligne[3][0:2] + " " +ligne[3][2:])
                if (l) % 3 == 2:
                    INC.append(ligne[2])
                    print(INC)
                    RAAN.append(ligne[3])
                    print(RAAN)
                    ECC.append(ligne[4])
                    AoP.append(ligne[5])
                    MA.append(ligne[6])
                    MM.append(ligne[7])

    print(f"noms des satellites: {sat} \n, INC : {INC} \n, RAAN : {RAAN} \n, ECC : {ECC} \n, AoP : {AoP} \n, MA : {MA} \n, MM : {MM} \n, Epoch : {Epoch} \n, ")

def exo14():
    fichier = input("merci d'indiquer le nom du fichier a créer (défaut: exercice_quatorze) : ")
    if len(fichier) == 0:
        fichier = "exercice_quatorze"
    fichier = fichier+".txt"

    txt = open(fichier, mode='w')
    txt.write(f"Exercice 1 : {exo1()}\nExercice 2 : {exo2()}\nExercice 3 : {exo3()}\nExercice 4 : {exo4()}\nExercice 5 : {exo5()}\nExercice 6 : {exo6()}")
    txt.close()

def exo15():
    fichier = input("merci d'indiquer le nom du fichier TLE (défaut: exercice_quatorze) : ")
    if len(fichier) == 0:
        fichier = "exercice_quatorze"
    fichier2 = fichier + "_copie.txt"
    fichier = fichier+".txt"

    f1 = open(fichier, mode="r")
    txt = f1.read()
    f1.close()

    f2 = open(fichier2, mode="w")
    f2.write(txt)
    f2.close()

    f2 = open(fichier2, mode="r")
    print(f2.read())
    f2.close()

def exo16():
    import csv
    import statistics
    fichier = input("fichier .csv à ouvrir : ")
    if len(fichier) == 0:
        fichier = "exemple"
    fichier = fichier + ".csv"
    menu = int(input(f"1. Afficher les données\n2. Effectuer un traitement\n"))
    if menu == 1:
        f1 = open(fichier, mode="r")
        txt = f1.read()
        print(txt)

        txt2 = csv.reader(f1)
        for line in txt2:
            print(line[3])
        f1.close()

    if menu == 2:
        f1 = open(fichier)
        txt2 = csv.reader(f1)

        colone = int(input("colone à modifier"))
        menu = int(input(f"1. Calculer la somme\n2. Calculer la moyenne\n3. Trouver la valeur minimale\n4. Trouver la valeur maximale\n"))
        nb = []
        mk=0
        for line in txt2 :
            try: nb.append(int(line[(colone - 1)]))
            except: continue
            """                
            if mk == 0 :
                mk = 1
                continue
            nb.append(int(line[(colone - 1)]))"""
        print(nb)
        match menu :
            case 1:
                tot = sum(nb)
            case 2:
                tot = sum(nb)/len(nb)
            case 3:
                tot = min(nb)
            case 4:
                tot = max(nb)
        print(tot)

def exo72():
    carac = False
    nb = False
    while carac==False or nb == False:
        mdp = (input("Nouveau Mot de Passe : "))

        if len(mdp)>7:
            nb = True
        for c in range(len(mdp)):
            if mdp[c] == "!" or mdp[c] == "@" or mdp[c] == "#" or mdp[c] == "$":
                carac = True

        if nb == False:
            print("8 caractères minimum")
            carac=False
        if carac == False:
            print("au moins 1 caractère spécial par exemple, !, @, #, $")
            nb=False

    print ("mdp valide")

def exo17():
    valid = False
    essai=0
    while valid==False :
        try:
            nb = int(input("Entrez un nombre entier : "))
            valid = True
        except :
            if essai > 5:
                print("Tu le fais exprès?")
            if essai > 10:
                print("ou alors ton clavier a un problème?")
            print("Je répete ... ")
            essai = essai+1
    tot = 0
    for x in range(nb):
        if (x%3==0) or (x%5==0):
            tot=tot+x
    print(tot)

def exo18():
    mot2=""
    mot = input("Entrez un mot a inverser : ")
    for x in reversed(mot):
        mot2=mot2+x
    print(mot2)

#main
"""
exo1()
exo2()
exo3()
exo4()
exo5()
exo6()
exo7()
exo8()
exo9()
exo10()
exo11()
exo12()
exo13()
exoTLE()
exo14()
exo15()
exo16()
exo72()
exo17()
"""
exo18()


