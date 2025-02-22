import tkinter as tk
from tkinter import messagebox
from constraint import *
from school_data_management import *
from school_data_management import teachers as teachers_data, school_data
from UI import teachers, classes

class SchoolRoutineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("School Routine Management System")

        # UI Elements
        self.label = tk.Label(root, text="School Routine Management", font=("Arial", 16))
        self.label.pack(pady=10)

        # Frame for buttons
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Class button
        self.add_class_button = tk.Button(self.frame, text="Add Class", command=self.add_class_ui)
        self.add_class_button.grid(row=0, column=0, padx=10, pady=10)

        # Subject button
        self.add_subject_button = tk.Button(self.frame, text="Add Subject", command=self.add_subject_ui)
        self.add_subject_button.grid(row=0, column=1, padx=10, pady=10)

        # Teacher button
        self.add_teacher_button = tk.Button(self.frame, text="Add Teacher", command=self.add_teacher_ui)
        self.add_teacher_button.grid(row=1, column=0, padx=10, pady=10)

        # Show Classes button
        self.show_classes_button = tk.Button(self.frame, text="Show Classes", command=self.show_classes)
        self.show_classes_button.grid(row=2, column=0, padx=10, pady=10)

        # Show Teachers button
        self.show_teachers_button = tk.Button(self.frame, text="Show Teachers", command=self.show_teachers)
        self.show_teachers_button.grid(row=2, column=1, padx=10, pady=10)

        # Generate Schedule button
        self.generate_schedule_button = tk.Button(self.frame, text="Generate Schedule", command=self.generate_schedule_ui)
        self.generate_schedule_button.grid(row=3, column=1, padx=10, pady=10)

        # Add Class to Teacher button
        self.add_class_to_teacher_button = tk.Button(self.frame, text="Add Class to Teacher", command=self.add_class_to_teacher_ui)
        self.add_class_to_teacher_button.grid(row=1, column=1, padx=10, pady=10)

        # Add Subject to Class for Teacher button
        self.add_subject_to_class_for_teacher_button = tk.Button(self.frame, text="Add Subject to Teacher for Class", command=self.add_subject_to_class_for_teacher_ui)
        self.add_subject_to_class_for_teacher_button.grid(row=3, column=0, padx=10, pady=10)

        # Set Number of Shifts button
        self.set_num_shifts_button = tk.Button(self.frame, text="Set Number of Shifts", command=self.add_num_shifts_ui)
        self.set_num_shifts_button.grid(row=4, column=0, padx=10, pady=10)


        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)
        
    def add_class_ui(self):
        self.new_class_window = tk.Toplevel(self.root)
        self.new_class_window.title("Add Class")

        self.class_name_label = tk.Label(self.new_class_window, text="Class Name:")
        self.class_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.class_name_entry = tk.Entry(self.new_class_window)
        self.class_name_entry.grid(row=0, column=1, padx=10)

        self.add_class_btn = tk.Button(self.new_class_window, text="Add", command=self.add_class)
        self.add_class_btn.grid(row=1, columnspan=2, pady=10)

    def add_class(self):
        class_name = self.class_name_entry.get()
        if class_name:
            add_class(class_name)
            messagebox.showinfo("Success", f"Class '{class_name}' added.")
            self.new_class_window.destroy()
        else:
            messagebox.showerror("Error", "Class name cannot be empty.")

    def add_subject_ui(self):
        self.new_subject_window = tk.Toplevel(self.root)
        self.new_subject_window.title("Add Subject")

        self.class_name_label = tk.Label(self.new_subject_window, text="Class Name:")
        self.class_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.class_name_entry = tk.Entry(self.new_subject_window)
        self.class_name_entry.grid(row=0, column=1, padx=10)

        self.subject_label = tk.Label(self.new_subject_window, text="Subject:")
        self.subject_label.grid(row=1, column=0, padx=10, pady=10)

        self.subject_entry = tk.Entry(self.new_subject_window)
        self.subject_entry.grid(row=1, column=1, padx=10)

        self.days_label = tk.Label(self.new_subject_window, text="Days per Week:")
        self.days_label.grid(row=2, column=0, padx=10, pady=10)

        self.days_entry = tk.Entry(self.new_subject_window)
        self.days_entry.grid(row=2, column=1, padx=10)

        self.add_subject_btn = tk.Button(self.new_subject_window, text="Add", command=self.add_subject)
        self.add_subject_btn.grid(row=3, columnspan=2, pady=10)

    def add_subject(self):
        class_name = self.class_name_entry.get()
        subject = self.subject_entry.get()
        try:
            days = int(self.days_entry.get())
            add_subject(class_name, subject, days)
            messagebox.showinfo("Success", f"Subject '{subject}' added to class '{class_name}' with {days} days.")
            self.new_subject_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Days per week must be a number.")

    def add_teacher_ui(self):
        self.new_teacher_window = tk.Toplevel(self.root)
        self.new_teacher_window.title("Add Teacher")

        self.teacher_name_label = tk.Label(self.new_teacher_window, text="Teacher Name:")
        self.teacher_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.teacher_name_entry = tk.Entry(self.new_teacher_window)
        self.teacher_name_entry.grid(row=0, column=1, padx=10)

        self.add_teacher_btn = tk.Button(self.new_teacher_window, text="Add", command=self.add_teacher)
        self.add_teacher_btn.grid(row=1, columnspan=2, pady=10)

    def add_teacher(self):
        teacher_name = self.teacher_name_entry.get()
        if teacher_name:
            add_teacher(teacher_name)
            messagebox.showinfo("Success", f"Teacher '{teacher_name}' added.")
            self.new_teacher_window.destroy()
        else:
            messagebox.showerror("Error", "Teacher name cannot be empty.")

    def show_classes(self):
        classes_window = tk.Toplevel(self.root)  # Create a new window
        classes.ClassesWindow(classes_window, school_data)

    def show_teachers(self):
        teachers_window = tk.Toplevel(self.root)  # Create a new window
        teachers.TeacherWindow(teachers_window, teachers_data)

    def generate_schedule_ui(self):
        self.result_label.config(text="Generating schedule...")
        status = self.generate_schedule()

        if status == "No feasible solution found!":
            messagebox.showerror("Error", status)
        else:
            messagebox.showinfo("Success", "Schedule generated successfully!")

    def generate_schedule(self):
        sm = scheduleMaker()
        sm.generate_schedule()
        # Call your existing schedule generation function here
        # For now, this is a placeholder that returns the success message
        return "Schedule generated."
    
    def add_class_to_teacher_ui(self):
        self.add_class_teacher_window = tk.Toplevel(self.root)
        self.add_class_teacher_window.title("Add Class to Teacher")

        self.teacher_name_label = tk.Label(self.add_class_teacher_window, text="Teacher Name:")
        self.teacher_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.teacher_name_entry = tk.Entry(self.add_class_teacher_window)
        self.teacher_name_entry.grid(row=0, column=1, padx=10)

        self.class_name_label = tk.Label(self.add_class_teacher_window, text="Class Name:")
        self.class_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.class_name_entry = tk.Entry(self.add_class_teacher_window)
        self.class_name_entry.grid(row=1, column=1, padx=10)

        self.add_class_teacher_btn = tk.Button(self.add_class_teacher_window, text="Add", command=self.add_class_to_teacher)
        self.add_class_teacher_btn.grid(row=2, columnspan=2, pady=10)

    def add_class_to_teacher(self):
        teacher_name = self.teacher_name_entry.get()
        class_name = self.class_name_entry.get()
        if teacher_name and class_name:
            add_class_to_teacher(teacher_name, class_name)
            messagebox.showinfo("Success", f"Class '{class_name}' added to teacher '{teacher_name}'.")
            self.add_class_teacher_window.destroy()
        else:
            messagebox.showerror("Error", "Teacher name and Class name cannot be empty.")

    def add_subject_to_class_for_teacher_ui(self):
        self.add_subject_teacher_class_window = tk.Toplevel(self.root)
        self.add_subject_teacher_class_window.title("Add Subject to Teacher for Class")

        self.teacher_name_label = tk.Label(self.add_subject_teacher_class_window, text="Teacher Name:")
        self.teacher_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.teacher_name_entry = tk.Entry(self.add_subject_teacher_class_window)
        self.teacher_name_entry.grid(row=0, column=1, padx=10)

        self.class_name_label = tk.Label(self.add_subject_teacher_class_window, text="Class Name:")
        self.class_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.class_name_entry = tk.Entry(self.add_subject_teacher_class_window)
        self.class_name_entry.grid(row=1, column=1, padx=10)

        self.subject_name_label = tk.Label(self.add_subject_teacher_class_window, text="Subject Name:")
        self.subject_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.subject_name_entry = tk.Entry(self.add_subject_teacher_class_window)
        self.subject_name_entry.grid(row=2, column=1, padx=10)

        self.add_subject_teacher_class_btn = tk.Button(self.add_subject_teacher_class_window, text="Add", command=self.add_subject_to_class_for_teacher)
        self.add_subject_teacher_class_btn.grid(row=3, columnspan=2, pady=10)

    def add_subject_to_class_for_teacher(self):
        teacher_name = self.teacher_name_entry.get()
        class_name = self.class_name_entry.get()
        subject_name = self.subject_name_entry.get()
        if teacher_name and class_name and subject_name:
            add_subject_to_class_for_teacher(teacher_name, class_name, subject_name)
            messagebox.showinfo("Success", f"Subject '{subject_name}' added to class '{class_name}' for teacher '{teacher_name}'.")
            self.add_subject_teacher_class_window.destroy()
        else:
            messagebox.showerror("Error", "Teacher name, Class name and Subject name cannot be empty.")

    def add_num_shifts_ui(self):
        self.add_num_shifts_window = tk.Toplevel(self.root)
        self.add_num_shifts_window.title("Set Number of Shifts")

        self.num_shifts_label = tk.Label(self.add_num_shifts_window, text="Number of Shifts:")
        self.num_shifts_label.grid(row=0, column=0, padx=10, pady=10)
        self.num_shifts_entry = tk.Entry(self.add_num_shifts_window)
        self.num_shifts_entry.grid(row=0, column=1, padx=10)

        self.add_num_shifts_btn = tk.Button(self.add_num_shifts_window, text="Set", command=self.add_num_shifts)
        self.add_num_shifts_btn.grid(row=1, columnspan=2, pady=10)

    def add_num_shifts(self):
        try:
            num_shifts = int(self.num_shifts_entry.get())
            if num_shifts > 0:
                add_num_shifts(num_shifts)
                messagebox.showinfo("Success", f"Number of shifts set to {num_shifts}.")
                self.add_num_shifts_window.destroy()
            else:
                messagebox.showerror("Error", "Number of shifts must be greater than 0.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of shifts. Must be a number.")
