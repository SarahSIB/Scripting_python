import json
from pathlib import Path

TITRE_APPLICATION = "MON ORGANISEUR - TO DO LIST"
FICHIER_TACHES = Path("taches.json")

def charger_donnees():
    """Charge les taches depuis le fichier JSON s'il existe."""
    if FICHIER_TACHES.exists():
        with open(FICHIER_TACHES, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder_donnees(collection):
    """Sauvegarde la collection dans le fichier JSON."""
    with open(FICHIER_TACHES, "w", encoding="utf-8") as f:
        json.dump(collection, f, indent=4)

def afficher_menu():
    """Affiche les options dispo dans le script."""
    print(f"\n=== {TITRE_APPLICATION} ===")
    print("1. Lister | 2. Ajouter | 3. Terminer | 4. Supprimer | 5. Quitter")

def lister_taches(collection):
    """
    Parcours la liste des taches avec une boucle for.
    Affiche le statut qui se base suru n type booléen.
    """
    print("\nLISTE DES TACHES :")
    if not collection:
        print("aucune tache a faire.")
    else:
        for i, item in enumerate(collection, start=1):
            statut = "✅" if item["faite"] else "❌"
            print(f"{i}. {item['tache']} [{statut}]")

def ajouter_tache(collection):
    """permet de creer un dict pour décrire l'artefact et l'ajoute à la liste."""
    nom = input("nom de la tache a ajouter : ")
    if nom:
        nouvelle = {"tache": nom, "faite": False}
        collection.append(nouvelle)
        sauvegarder_donnees(collection)
        print("tache ajoutée.")

def modifier_statut(collection):
    """Gère les erreurs avec try/except en cas de mauvaise saisie."""
    try:
        choix = int(input("numéro de la tache terminée : "))
        collection[choix - 1]["faite"] = True
        sauvegarder_donnees(collection)
        print("le statut de la tâche a été mis à jour.")
    except (ValueError, IndexError):
        print("erreur : numéro invalide, recommencer.")

def supprimer_tache(collection):
    """Supprime un élément de la collection et met à jour le fichier."""
    try:
        choix = int(input("Numero de la tache a supprimer : "))
        collection.pop(choix - 1)
        sauvegarder_donnees(collection)
        print("Tache supprimée.")
    except (ValueError, IndexError):
        print("erreur : Impossible de supprimer cet elément.")

if __name__ == "__main__":
    taches = charger_donnees()
    
    en_cours = True
    while en_cours:
        afficher_menu()
        choix_utilisateur = input("\n que voulez vous choisir : ")

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
            print("Vous avez choisi de quitter le programme.")
        else:
            print("option non reconnue.")