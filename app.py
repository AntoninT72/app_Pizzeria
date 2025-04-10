# app.py

import customtkinter as ctk
import api

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class PizzeriaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pizzeria - Gestion des Produits")
        self.geometry("600x500")
        self.resizable(False, False)

        # Entrées
        self.nom_entry = ctk.CTkEntry(self, placeholder_text="Nom de la pizza")
        self.nom_entry.pack(pady=10)

        self.prix_entry = ctk.CTkEntry(self, placeholder_text="Prix (€)")
        self.prix_entry.pack(pady=10)

        self.add_btn = ctk.CTkButton(self, text="Ajouter une pizza", command=self.ajouter_pizza)
        self.add_btn.pack(pady=10)

        # Liste des pizzas
        self.pizza_listbox = ctk.CTkTextbox(self, width=500, height=250)
        self.pizza_listbox.pack(pady=10)

        # Suppression
        self.delete_id_entry = ctk.CTkEntry(self, placeholder_text="ID à supprimer")
        self.delete_id_entry.pack(pady=5)

        self.delete_btn = ctk.CTkButton(self, text="Supprimer la pizza", command=self.supprimer_pizza)
        self.delete_btn.pack(pady=5)

        # Rafraîchir
        self.refresh_btn = ctk.CTkButton(self, text="Actualiser la liste", command=self.afficher_pizzas)
        self.refresh_btn.pack(pady=5)

        # Démarrage
        self.afficher_pizzas()

    def afficher_pizzas(self):
        self.pizza_listbox.delete("1.0", "end")
        pizzas = api.get_all_products()
        for p in pizzas:
            self.pizza_listbox.insert("end", f"{p['id']} - {p['nom']} : {p['prix']} €\n")

    def ajouter_pizza(self):
        nom = self.nom_entry.get()
        prix = self.prix_entry.get()
        try:
            prix = float(prix)
            api.add_product(nom, prix)
            self.nom_entry.delete(0, "end")
            self.prix_entry.delete(0, "end")
            self.afficher_pizzas()
        except ValueError:
            self.pizza_listbox.insert("end", "⚠️ Prix invalide\n")

    def supprimer_pizza(self):
        try:
            pizza_id = int(self.delete_id_entry.get())
            api.delete_product(pizza_id)
            self.delete_id_entry.delete(0, "end")
            self.afficher_pizzas()
        except ValueError:
            self.pizza_listbox.insert("end", "⚠️ ID invalide\n")

if __name__ == "__main__":
    app = PizzeriaApp()
    app.mainloop()
