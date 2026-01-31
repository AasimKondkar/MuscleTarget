import tkinter as tk
from tkinter import ttk
from exercises import muscle_db


class MuscleTargetGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("MuscleTarget 💪")
        self.root.geometry("500x450")

        # Body Part Dropdown
        tk.Label(root, text="Select Body Part").pack(pady=5)

        self.body_var = tk.StringVar()
        self.body_combo = ttk.Combobox(root, textvariable=self.body_var, state="readonly")
        self.body_combo["values"] = list(muscle_db.keys())
        self.body_combo.pack()

        self.body_combo.bind("<<ComboboxSelected>>", self.update_sub_parts)

        # Sub Part Dropdown
        tk.Label(root, text="Select Target Area").pack(pady=5)

        self.sub_var = tk.StringVar()
        self.sub_combo = ttk.Combobox(root, textvariable=self.sub_var, state="readonly")
        self.sub_combo.pack()

        # Button
        tk.Button(root, text="Show Exercises", command=self.show_exercises).pack(pady=10)

        # Output Box
        self.output = tk.Text(root, height=15, width=55)
        self.output.pack(pady=10)

    def update_sub_parts(self, event):
        body = self.body_var.get()
        sub_parts = list(muscle_db[body].keys())
        self.sub_combo["values"] = sub_parts
        self.sub_combo.set("")

    def show_exercises(self):
        body = self.body_var.get()
        sub = self.sub_var.get()

        self.output.delete("1.0", tk.END)

        if not body or not sub:
            self.output.insert(tk.END, "Please select both body part and target area.")
            return

        exercises = muscle_db[body][sub]

        self.output.insert(tk.END, f"{body} → {sub}\n\n")

        for i, ex in enumerate(exercises, start=1):
            self.output.insert(tk.END, f"{i}. {ex}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MuscleTargetGUI(root)
    root.mainloop()
