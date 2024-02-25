import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Scientific Calculator")

        self.text_entry = tk.Entry(root, justify="right")
        self.text_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "sqrt", "pow", "sin", "cos", "tan"
        ]

        row, col = 1, 0
        for btn_text in buttons:
            button = tk.Button(root, text=btn_text, command=lambda t=btn_text: self.on_button_click(t))
            button.grid(row=row, column=col)
            col = (col + 1) % 4
            if col == 0:
                row += 1

    def on_button_click(self, btn_text):
        current_text = self.text_entry.get()

        if btn_text == "=":
            try:
                result = eval(current_text)
                self.text_entry.delete(0, tk.END)
                self.text_entry.insert(0, str(result))
            except Exception:
                self.text_entry.delete(0, tk.END)
                self.text_entry.insert(0, "Error")
        elif btn_text == "sqrt":
            self.text_entry.insert(tk.END, "sqrt(")
        elif btn_text == "pow":
            self.text_entry.insert(tk.END, "**")
        elif btn_text in ["sin", "cos", "tan"]:
            self.text_entry.insert(tk.END, f"{btn_text}(")
        else:
            self.text_entry.insert(tk.END, btn_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
