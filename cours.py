"""
Projet : MonOrganiseur
Description : Automatisation de la gestion de tâches (artefacts)
"""

import tkinter as tk
from tkinter import messagebox


TITRE_APPLICATION = "MonOrganiseur - Scripting Python"


def ajouter_tache(entree, liste_donnees, listbox):
    """
    Ajoute un artefact à la collection de données.
    Utilise le type 'str' pour la description. 
    """
    tache_texte = entree.get()
    
    if tache_texte.strip() == "":
        messagebox.showwarning("Erreur", "La tâche est vide !")
        return

    nouvel_artefact = {"tache": tache_texte, "faite": False}
    liste_donnees.append(nouvel_artefact)
    
    entree.delete(0, tk.END)
    actualiser_affichage(liste_donnees, listbox)

def actualiser_affichage(liste_donnees, listbox):
    """
    Parcourt la collection (List) pour mettre à jour l'interface. 
    Utilise une boucle 'for'. [cite: 20]
    """
    listbox.delete(0, tk.END)
    for index, artefact in enumerate(liste_donnees, start=1):
        # Utilisation de booléens pour le statut 
        statut = "✅" if artefact["faite"] else "❌"
        listbox.insert(tk.END, f"{index}. {artefact['tache']} [{statut}]")

def marquer_terminee(liste_donnees, listbox):
    """
    Gère les erreurs avec try/except pour la sélection. [cite: 25]
    """
    try:
        selection = listbox.curselection()
        if not selection:
            raise IndexError("Aucun élément sélectionné")
            
        index = selection[0]
        liste_donnees[index]["faite"] = True
        actualiser_affichage(liste_donnees, listbox)
    except IndexError:
        messagebox.showwarning("Attention", "Sélectionnez une tâche.")



if __name__ == "__main__":
    taches = []   

    
    root = tk.Tk()
    root.title(TITRE_APPLICATION)

    entree_tache = tk.Entry(root, width=40)
    entree_tache.pack(pady=10)

    btn_ajout = tk.Button(root, text="Ajouter", 
                          command=lambda: ajouter_tache(entree_tache, taches, liste_visuelle))
    btn_ajout.pack()

    liste_visuelle = tk.Listbox(root, width=50)
    liste_visuelle.pack(pady=10)

    btn_ok = tk.Button(root, text="Marquer Faite", 
                       command=lambda: marquer_terminee(taches, liste_visuelle))
    btn_ok.pack()

    root.mainloop()