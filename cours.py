import tkinter as tk
from tkinter import messagebox

# --- CONSTANTES ---
TITRE_APP = "MonOrganiseur - To-Do List"

# --- LOGIQUE (FONCTIONS) ---

def actualiser_liste():
    """Utilise une boucle for pour rafraîchir l'affichage."""
    listbox_visuelle.delete(0, tk.END)
    for index, item in enumerate(taches_donnees, start=1):
        # Utilisation de booleens (True/False) comme vu en cours
        statut = "✅" if item["faite"] else "❌"
        listbox_visuelle.insert(tk.END, f"{index}. {item['tache']} [{statut}]")

def ajouter_tache():
    Texte = entree.get().strip()
    if Texte:
        # On crée un dictionnaire (dict) pour l'artefact
        nouvelle_tache = {"tache": Texte, "faite": False}
        taches_donnees.append(nouvelle_tache)
        entree.delete(0, tk.END)
        actualiser_liste()
    else:
        messagebox.showwarning("Erreur", "Le champ est vide !")

def marquer_terminee():
    """Bascule le statut 'faite' en utilisant try/except."""
    try:
        selection = listbox_visuelle.curselection()
        index = selection[0]
        # On modifie la valeur dans le dictionnaire
        taches_donnees[index]["faite"] = True
        actualiser_liste()
    except IndexError:
        messagebox.showinfo("Info", "Sélectionnez une tâche à valider.")

def supprimer_tache():
    """Supprime l'élément de la liste (List)."""
    try:
        selection = listbox_visuelle.curselection()
        index = selection[0]
        # .pop() retire l'élément de la collection
        taches_donnees.pop(index)
        actualiser_liste()
    except IndexError:
        messagebox.showwarning("Erreur", "Sélectionnez une tâche à supprimer.")

# --- INTERFACE (MAIN) ---
if __name__ == "__main__":
    # Notre collection de données (List)
    taches_donnees = []

    fenetre = tk.Tk()
    fenetre.title(TITRE_APP)

    entree = tk.Entry(fenetre, width=40)
    entree.pack(pady=10)

    # Bouton pour AJOUTER
    tk.Button(fenetre, text="Ajouter la tâche", command=ajouter_tache).pack(pady=2)

    listbox_visuelle = tk.Listbox(fenetre, width=50)
    listbox_visuelle.pack(pady=10)

    # Bouton pour TERMINER (Le bouton "OK")
    tk.Button(fenetre, text="Marquer comme terminée (OK)", 
              fg="green", command=marquer_terminee).pack(pady=2)

    # Bouton pour SUPPRIMER
    tk.Button(fenetre, text="Supprimer la tâche", 
              fg="red", command=supprimer_tache).pack(pady=2)

    fenetre.mainloop()