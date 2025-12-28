import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# -------------------- Main Application -------------------- #
class PasswordGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("480x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f8")

        self.setup_style()
        self.create_ui()

    # -------------------- Styling -------------------- #
    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TLabel",
            font=("Segoe UI", 11),
            background="#ffffff"
        )

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 20, "bold"),
            foreground="#2c3e50",
            background="#f4f6f8"
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 11, "bold"),
            padding=10
        )

        style.configure(
            "Generate.TButton",
            background="#2ecc71",
            foreground="white"
        )

        style.map(
            "Generate.TButton",
            background=[("active", "#27ae60")]
        )

        style.configure(
            "Card.TFrame",
            background="#ffffff",
            relief="flat"
        )

        style.configure(
            "TCheckbutton",
            background="#ffffff",
            font=("Segoe UI", 10)
        )

    # -------------------- UI Layout -------------------- #
    def create_ui(self):
        # Title
        title = ttk.Label(
            self.root,
            text="Secure Password Generator",
            style="Title.TLabel"
        )
        title.pack(pady=20)

        # Card Container
        card = ttk.Frame(self.root, style="Card.TFrame")
        card.pack(padx=25, pady=10, fill="both", expand=True)

        # Password Length
        ttk.Label(card, text="Password Length").pack(anchor="w", pady=(15, 5), padx=20)
        self.length_var = tk.StringVar()
        length_entry = ttk.Entry(card, textvariable=self.length_var, width=15)
        length_entry.pack(anchor="w", padx=20)

        # Options
        ttk.Label(card, text="Include Characters").pack(anchor="w", pady=(20, 5), padx=20)

        self.uppercase = tk.BooleanVar(value=True)
        self.lowercase = tk.BooleanVar(value=True)
        self.numbers = tk.BooleanVar(value=True)
        self.symbols = tk.BooleanVar()

        ttk.Checkbutton(card, text="Uppercase Letters (A-Z)", variable=self.uppercase).pack(anchor="w", padx=20)
        ttk.Checkbutton(card, text="Lowercase Letters (a-z)", variable=self.lowercase).pack(anchor="w", padx=20)
        ttk.Checkbutton(card, text="Numbers (0-9)", variable=self.numbers).pack(anchor="w", padx=20)
        ttk.Checkbutton(card, text="Symbols (!@#$)", variable=self.symbols).pack(anchor="w", padx=20)

        # Generate Button
        generate_btn = ttk.Button(
            card,
            text="Generate Password",
            style="Generate.TButton",
            command=self.generate_password
        )
        generate_btn.pack(pady=25)

        # Output
        ttk.Label(card, text="Generated Password").pack(anchor="w", padx=20)
        self.result_entry = ttk.Entry(card, font=("Consolas", 12))
        self.result_entry.pack(fill="x", padx=20, pady=(5, 20))

        # Footer
        footer = ttk.Label(
            self.root,
            text="Python Tkinter Project • Internship Ready",
            font=("Segoe UI", 9),
            background="#f4f6f8",
            foreground="#7f8c8d"
        )
        footer.pack(pady=10)

    # -------------------- Logic -------------------- #
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Password length must be a number ≥ 4")
            return

        characters = ""
        if self.uppercase.get():
            characters += string.ascii_uppercase
        if self.lowercase.get():
            characters += string.ascii_lowercase
        if self.numbers.get():
            characters += string.digits
        if self.symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Selection Required", "Select at least one character type")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)


# -------------------- Run Application -------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
