import tkinter as tk


class Card(tk.Frame):

    def __init__(self, parent, titre, valeur, couleur):

        super().__init__(
            parent,
            bg=couleur,
            width=220,
            height=100
        )

        self.pack_propagate(False)

        tk.Label(
            self,
            text=titre,
            bg=couleur,
            fg="white",
            font=("Segoe UI", 11)
        ).pack(
            pady=(15, 5)
        )

        self.valeur = tk.Label(
            self,
            text=str(valeur),
            bg=couleur,
            fg="white",
            font=("Segoe UI", 22, "bold")
        )

        self.valeur.pack()

    def mettre_a_jour(self, valeur):

        self.valeur.config(text=str(valeur))