import tkinter as tk
from tkinter import messagebox
import gmpy2

class CalculatorPrim:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Verificare Număr Prim")

        # Crearea unui câmp Text mai mare pentru introducerea numerelor
        self.label = tk.Label(self.root, text="Introdu un număr:")
        self.label.pack(pady=5)

        self.text_input = tk.Text(self.root, height=2, width=40)  # Larger input area
        self.text_input.pack(pady=10)

        # Crearea butonului de verificare
        self.button = tk.Button(self.root, text="Verifică", command=self.verifica_prim)
        self.button.pack(pady=10)

    # Funcție pentru a verifica dacă un număr este prim folosind gmpy2
    def este_prim(self, numar):
        # Use gmpy2 to check if the number is prime efficiently
        return gmpy2.is_prime(numar)

    # Funcție care se activează la apăsarea butonului
    def verifica_prim(self):
        try:
            input_text = self.text_input.get("1.0", tk.END).strip()  # Preia textul din câmp
            numar = gmpy2.mpz(input_text)  # Convertim numărul într-un mpz (număr întreg cu precizie mare)

            if self.este_prim(numar):
                messagebox.showinfo("Rezultat", f"{numar} este un număr prim!")
            else:
                messagebox.showinfo("Rezultat", f"{numar} nu este un număr prim.")
        except ValueError:
            messagebox.showerror("Eroare", "Te rog introdu un număr întreg valid!")

    # Funcție pentru a rula aplicația
    def run(self):
        self.root.mainloop()
