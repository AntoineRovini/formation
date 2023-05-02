pi=3.14

def exo1():
    C=float(input("temperature en °C"))
    F=(C*9/5)+32
    print(F)

def exo2():
    R = float(input("rayon du cercle"))
    A=pi*(R**2)
    print(A)

def exo3():
    nombres = [int(input("nombre1")),int(input("nombre2")),int(input("nombre3"))]
    moy = (nombres[0]+nombres[1]+nombres[2])/3
    print(moy)

def exo4():
    nombre = int(input("nombre entier"))
    reste = nombre%2
    if reste == 0 :
        print("pair")
    else:
        print("impair")

def exo5():
    nombre = int(input("nombre entier"))
    tot=0
    while nombre>0:
        tot=tot+nombre
        nombre=nombre-1
    print(tot)

def exo6():
    nombres = (input("nombres séparés par des virgules"))
    n = [int(x) for x in nombres.split(",")]
    moy=sum(n)/len(n)
    print(moy)

def exo7():
    mdp = (input("Nouveau Mot de Passe"))
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
    B = int(input("trouvez le chiffre entre 1 et 100"))

    while A != B:
        if A < B :
            print("trop grand")
        if A > B:
            print("trop petit")
        B = int(input("trouvez le chiffre entre 1 et 100"))
    print("Bravo !")

def exo9():
    import random

    A = random.choice(seq=["un", "deux", "trois"])
    B = input("trouvez le bon mot")
    C = 0
    D = len(A)
    while C < D:
        if A == B :
            print("Bravo !")
            C=D
        if A != B:
            print("raté, voici un indice : ", A[C])
            B = input("trouvez le bon mot")
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
