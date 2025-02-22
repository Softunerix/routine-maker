import tkinter as tk

class TeacherWindow:
    def __init__(self, root, teachers):
        self.root = root
        self.root.title("Teachers and Subjects")

        self.teachers = teachers  # Store the teachers' data
        self.create_ui()

    def create_ui(self):
        row = 0
        for teacher, classes in self.teachers.items():
            # Display teacher name
            tk.Label(self.root, text=teacher, font=("Arial", 12, "bold")).grid(row=row, column=0, padx=10, pady=5, sticky="w")
            row += 1

            for class_name, subjects in classes.items():
                subject_text = ", ".join(subjects) if subjects else "No subjects"
                display_text = f"{class_name}: {subject_text}"
                
                tk.Label(self.root, text=display_text, font=("Arial", 10)).grid(row=row, column=0, padx=20, pady=2, sticky="w")
                row += 1
