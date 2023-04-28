tasks = []

while True:
    print("Que voulez-vous faire?")
    print("1. Ajouter une tâche")
    print("2. Afficher toutes les tâches")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme terminée")
    print("5. Quitter")

    choice = input()

    if choice == "1":
        task = input("Entrez une tâche: ")
        tasks.append(task)
        print("Tâche ajoutée.")
    elif choice == "2":
        print("Voici toutes les tâches:")
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i])
    elif choice == "3":
        index = int(input("Entrez l'indice de la tâche à supprimer: ")) - 1
        del tasks[index]
        print("Tâche supprimée.")
    elif choice == "4":
        index = int(input("Entrez l'indice de la tâche terminée: ")) - 1
        tasks[index] = "[TERMINÉE] " + tasks[index]
        print("Tâche marquée comme terminée.")
    elif choice == "5":
        break
    else:
        print("Choix invalide.")