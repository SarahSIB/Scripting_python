import json
from pathlib import Path

TITRE_APPLICATION = "MON ORGANISEUR - TO DO LIST"
FICHIER_TACHES = Path("taches.json")

def charger_donnees():
    """Charge les tâches depuis le fichier JSON s'il existe."""
    if FICHIER_TACHES.exists():
        with open(FICHIER_TACHES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder_donnees(collection):
    """Sauvegarde la collection dans un fichier JSON avec indentation."""
    with open(FICHIER_TACHES, "w", encoding="utf-8") as f:
        json.dump(collection, f, indent=4)

def afficher_menu():
    """Affiche les options disponibles dans le script."""
    print(f"\n=== {TITRE_APPLICATION} ===")
    print("1. Lister | 2. Ajouter | 3. Terminer | 4. Supprimer | 5. Quitter")

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
            statut = "✅" if item["faite"] else "❌"
            print(f"{i}. {item['tache']} [{statut}]")

def ajouter_tache(collection):
    """Crée un dictionnaire (dict) pour décrire l'artefact et l'ajoute à la liste."""
    nom = input("Nom de la nouvelle tâche : ")
    if nom:
        nouvelle = {"tache": nom, "faite": False}
        collection.append(nouvelle)
        sauvegarder_donnees(collection)
        print("Tâche ajoutée.")

def modifier_statut(collection):
    """Gère les erreurs avec try/except en cas de mauvaise saisie."""
    try:
        choix = int(input("Numéro de la tâche terminée : "))
        collection[choix - 1]["faite"] = True
        sauvegarder_donnees(collection)
        print("Statut mis à jour.")
    except (ValueError, IndexError):
        print("Erreur : Numéro invalide.")

def supprimer_tache(collection):
    """Supprime un élément de la collection et met à jour le fichier."""
    try:
        choix = int(input("Numéro de la tâche à supprimer : "))
        collection.pop(choix - 1)
        sauvegarder_donnees(collection)
        print("Tâche supprimée.")
    except (ValueError, IndexError):
        print("Erreur : Impossible de supprimer cet élément.")

if __name__ == "__main__":
    taches = charger_donnees()
    
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