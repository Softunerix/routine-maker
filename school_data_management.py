# teacher -> class -> subjects (proficient in)
teachers = {
    "Alice": {"One": {"English", "Bengali"}, "Two": {"H. Math"}, "Three": {}},
    "Bob": {"One": {"Math"}, "Two": {"Math"}, "Three": {}},
    "Jolly": {"One": {}, "Two": {}, "Three": {"ICT", "Biology"}},
    "Mark": {"One": {}, "Two": {"Physics"}, "Three": {"BGS"}},
}

# class -> subject -> days (per week (required))
school_data = {
    "One": {"Math": 6, "English": 6, "Bengali": 6},
    "Two": {"Physics": 3, "H. Math": 2, "Math": 6},
    "Three": {"Biology": 3, "BGS": 3, "ICT": 3},
}

# Number of classes are open per week and number of shifts in a day
num_days = 6
num_shifts = 3

def add_class(class_name):
    """Adds a new class if it doesn't exist."""
    if class_name not in school_data:
        school_data[class_name] = {}


def add_subject(class_name, subject, days):
    """Adds a subject with the number of days to a class in school_data."""
    if class_name not in school_data:
        school_data[class_name] = {}  # Initialize as a dictionary, not a list.

    if subject in school_data[class_name]:
        print(f"Subject '{subject}' already exists in class '{class_name}'.")
        return

    school_data[class_name][subject] = int(days)

def add_teacher(teacher_name):
    """Add a new teacher to the dictionary."""
    if teacher_name not in teachers:
        teachers[teacher_name] = {}

def add_class_to_teacher(teacher_name, class_name):
    """Add a class to the teacher, along with subjects they can teach in that class."""
    if teacher_name not in teachers:
        print(f"Teacher {teacher_name} not found!")
        return

    # Initialize the teacher's class data if not already present
    if class_name not in teachers[teacher_name]:
        teachers[teacher_name][class_name] = set()
    else:
        print(f"Teacher {teacher_name} already has {class_name} assigned.")

def add_subject_to_class_for_teacher(teacher_name, class_name, subject):
    """Assign a subject to a class for a teacher."""
    if teacher_name not in teachers:
        print(f"Teacher {teacher_name} not found!")
        add_teacher(teacher_name)

    if class_name not in teachers[teacher_name]:
        print(f"Class {class_name} not assigned to {teacher_name} yet!")
        add_class_to_teacher(teacher_name, class_name)

    # Add the subject to the teacher's class
    teachers[teacher_name][class_name].add(subject)

def add_num_days(num_of_days):
    """Set the number of days in a week."""
    global num_days
    num_days = int(num_of_days)
    
def add_num_shifts(num_of_shifts):
    """Set the number of shifts in a day."""
    global num_shifts
    num_shifts = int(num_of_shifts)