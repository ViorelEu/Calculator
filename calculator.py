import tkinter as tk
from tkinter import messagebox


class CalculatorPrim:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Verificare Număr Prim")

        # Crearea câmpului de input
        self.entry = tk.Entry(self.root, validate="key")
        self.entry['validatecommand'] = (self.entry.register(self.validare_input), '%P')
        self.entry.pack(pady=10)

        # Crearea butonului de verificare
        self.button = tk.Button(self.root, text="Verifică", command=self.verifica_prim)
        self.button.pack(pady=10)

    # Funcție pentru a verifica dacă un număr este prim
    def este_prim(self, numar):
        if numar < 2:
            return False
        for i in range(2, int(numar ** 0.5) + 1):
            if numar % i == 0:
                return False
        return True

    # Funcție care se activează la apăsarea butonului
    def verifica_prim(self):
        try:
            numar = int(self.entry.get())  # Se asigură că intrarea este un număr întreg
            if self.este_prim(numar):
                messagebox.showinfo("Rezultat", f"{numar} este un număr prim!")
            else:
                messagebox.showinfo("Rezultat", f"{numar} nu este un număr prim.")
        except ValueError:
            messagebox.showerror("Eroare", "Te rog introdu un număr întreg valid!")

    # Funcție pentru a restricționa input-ul doar la numere întregi
    def validare_input(self, text):
        return text.isdigit() or text == ""

    # Funcție pentru a rula aplicația
    def run(self):
        self.root.mainloop()
