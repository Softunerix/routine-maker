import tkinter as tk

class ClassesWindow:
    def __init__(self, root, school_data):
        self.root = root
        self.root.title("Classes and Subjects")

        self.school_data = school_data  # Use the school_data directly
        self.create_ui()

    def create_ui(self):
        row = 0
        for class_name, subjects_data in self.school_data.items():
            # Display class name
            tk.Label(self.root, text=class_name, font=("Arial", 12, "bold")).grid(row=row, column=0, padx=10, pady=5, sticky="w")
            row += 1

            for subject, days in subjects_data.items():
                display_text = f"- {subject}: {days} days"
                tk.Label(self.root, text=display_text, font=("Arial", 10)).grid(row=row, column=0, padx=20, pady=2, sticky="w")
                row += 1

        if not self.school_data:
            tk.Label(self.root, text="No classes or subjects data available.", font=("Arial", 10)).grid(row=row, column=0, padx=10, pady=5, sticky="w")