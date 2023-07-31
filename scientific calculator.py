import tkinter as tk 
from math import *
class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")
        self.geometry("400x400")
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=("Helvetica", 18), bd=10, relief="ridge", justify="right")
        result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons for numbers and basic operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Helvetica", 18), bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Clear button
        clear_button = tk.Button(self, text="C", font=("Helvetica", 18), bd=5, command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Backspace button
        backspace_button = tk.Button(self, text="⌫", font=("Helvetica", 18), bd=5, command=self.backspace)
        backspace_button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

        # Advanced functions buttons
        functions = [
            ('sin', self.sin),
            ('cos', self.cos),
            ('tan', self.tan),
            ('sqrt', self.sqrt),
            ('^', lambda: self.on_button_click('**')),
            ('(', lambda: self.on_button_click('(')),
            (')', lambda: self.on_button_click(')')),
        ]

        for i, (text, func) in enumerate(functions):
            button = tk.Button(self, text=text, font=("Helvetica", 18), bd=5, command=func)
            button.grid(row=i // 2 + 6, column=i % 2, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, text):
        current_result = self.result_var.get()

        if text == "=":
            try:
                result = eval(current_result)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_result + text)

    def clear(self):
        self.result_var.set("")

    def backspace(self):
        current_result = self.result_var.get()
        self.result_var.set(current_result[:-1])

    def sin(self):
        try:
            value = eval(self.result_var.get())
            result = sin(value)
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")

    def cos(self):
        try:
            value = eval(self.result_var.get())
            result = cos(value)
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")

    def tan(self):
        try:
            value = eval(self.result_var.get())
            result = tan(value)
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")

    def sqrt(self):
        try:
            value = eval(self.result_var.get())
            result = sqrt(value)
            self.result_var.set(str(result))
        except Exception as e:
            self.result_var.set("Error")


if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
