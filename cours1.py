import os  # Pour les interactions système mentionnées dans le cours [cite: 82]

TITRE_APPLICATION = "MON ORGANISEUR - TO DO LIST"


def afficher_menu():
    """Affiche les options disponibles dans le script."""
 
    print("\n1. Lister les taches| 2. Ajouter  une tache| 3. Tache Terminée | 4. Supprimer une tache| 5. Quitter")

def lister_taches(collection):
    """
    Parcourt la liste des tâches avec une boucle for.
    Affiche le statut basé sur un type booléen.
    """
    print("\nLISTE DES TÂCHES :")
    if not collection:
        print("Aucune tâche pour le moment.")
    else:
        for i, item in enumerate(collection, start=1):
            # Utilisation de la logique if/else pour le statut 
            statut = "✅" if item["faite"] else "❌"
            print(f"{i}. {item['tache']} [{statut}]")

def ajouter_tache(collection):
    """Crée un dictionnaire (dict) pour décrire l'artefact."""
    nom = input("Nom de la nouvelle tâche : ")
    if nom:
        # Stockage sous forme de dictionnaire 
        nouvelle = {"tache": nom, "faite": False}
        collection.append(nouvelle)
        print("Tâche ajoutée.")

def modifier_statut(collection):
    """Gère les erreurs avec try/except en cas de mauvaise saisie[cite: 23, 25]."""
    try:
        choix = int(input("Numéro de la tâche terminée : "))
        # Accès à l'élément de la liste (List) 
        collection[choix - 1]["faite"] = True
        print("Statut mis à jour.")
    except (ValueError, IndexError):
        print("Erreur : Numéro invalide.")

def supprimer_tache(collection):
    """Supprime un élément de la collection."""
    try:
        choix = int(input("Numéro de la tâche à supprimer : "))
        collection.pop(choix - 1)
        print("Tâche supprimée.")
    except (ValueError, IndexError):
        print("Erreur : Impossible de supprimer cet élément.")

# --- 3. POINT D'ENTRÉE (Exécuté uniquement en lancement direct) -
if __name__ == "__main__":
    # Initialisation d'une liste (Collection) 
    taches = []
    
    # Utilisation d'une boucle while pour le contrôle de flux 
    en_cours = True
    while en_cours:
        afficher_menu()
        choix_utilisateur = input("\nVotre choix : ")

        if choix_utilisateur == "1":
            lister_taches(taches)
        elif choix_utilisateur == "2":
            ajouter_tache(taches)
        elif choix_utilisateur == "3":
            modifier_statut(taches)
        elif choix_utilisateur == "4":
            supprimer_tache(taches)
        elif choix_utilisateur == "5":
            en_cours = False
            print("Fermeture du script.")
        else:
            print("Option non reconnue.")