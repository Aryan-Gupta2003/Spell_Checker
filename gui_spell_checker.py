import tkinter as tk
from tkinter import filedialog, messagebox
from spell_checker import SpellChecker

class SpellCheckerGUI:
    def __init__(self, root, spell_checker):
        self.root = root
        self.spell_checker = spell_checker
        self.root.title("Spell Checker")

        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack(pady=5)

        self.result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
        self.result_text.pack(pady=10)

    def check_spelling(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        result = self.spell_checker.check_text(text)

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    spell_checker = SpellChecker('dictionary.txt')
    app = SpellCheckerGUI(root, spell_checker)
    root.mainloop()

if __name__ == "__main__":
    main()
