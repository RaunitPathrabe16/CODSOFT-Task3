import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.configure(bg='#add8e6')

        for i in range(9):
            root.columnconfigure(i, weight=1)
            root.rowconfigure(i, weight=1)
        
        self.label = tk.Label(root, text="Enter desired password length:", bg='#add8e6')
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.uppercase_var = tk.IntVar()
        self.lowercase_var = tk.IntVar()
        self.numbers_var = tk.IntVar()
        self.symbols_var = tk.IntVar()

        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=self.uppercase_var, bg='#add8e6')
        self.uppercase_check.grid(row=2, column=0, padx=10, pady=2, sticky="w")

        self.lowercase_check = tk.Checkbutton(root, text="Include Lowercase", variable=self.lowercase_var, bg='#add8e6')
        self.lowercase_check.grid(row=2, column=1, padx=10, pady=2, sticky="w")

        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.numbers_var, bg='#add8e6')
        self.numbers_check.grid(row=3, column=0, padx=10, pady=2, sticky="w")

        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var, bg='#add8e6')
        self.symbols_check.grid(row=3, column=1, padx=10, pady=2, sticky="w")

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#add8e6')
        self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be at least 1.")
        except ValueError as e:
            self.result_label.config(text=f"Error: {e}")
            return

        character_pool = ""
        if self.uppercase_var.get():
            character_pool += string.ascii_uppercase
        if self.lowercase_var.get():
            character_pool += string.ascii_lowercase
        if self.numbers_var.get():
            character_pool += string.digits
        if self.symbols_var.get():
            character_pool += string.punctuation

        if not character_pool:
            self.result_label.config(text="Error: Select at least one option.")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        self.result_label.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result_label.cget("text").replace("Generated Password: ", ""))
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

