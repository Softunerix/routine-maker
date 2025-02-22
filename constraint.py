import os
import csv
from ortools.sat.python import cp_model
from school_data_management import *

class scheduleMaker:
    def __init__(self):
        self.model = cp_model.CpModel()
        self.schedule = {}
        self.solver = cp_model.CpSolver()
        self.solution_collector = None

    def build_model(self):
        # Create decision variables
        for teacher in teachers:
            for clss, subjects in school_data.items():
                for subject, days in subjects.items():
                    if subject in teachers[teacher].get(clss, []):  # Ensuring teacher can teach subject
                        for day in range(num_days):
                            for shift in range(num_shifts):
                                self.schedule[(teacher, clss, subject, day, shift)] = self.model.NewBoolVar(
                                    f"{teacher}_{teacher}_{subject}_{day}_{shift}"
                                )

        # 1st Constraint: Teacher must teach exactly the required number of shifts for each subject
        for teacher in teachers:
            for clss, subjects in school_data.items():
                for subject, required_days in subjects.items():
                    if subject in teachers[teacher].get(clss, []):
                        self.model.Add(
                            sum(
                                self.schedule[(teacher, clss, subject, day, shift)]
                                for day in range(num_days)
                                for shift in range(num_shifts)
                            ) == required_days
                        )

        # 2nd Constraint: Teachers cannot teach subjects they are not qualified for 
        for teacher in teachers: 
            for clss, subjects in school_data.items(): 
                for subject in subjects.keys(): 
                    if subject not in teachers[teacher].get(clss, []): 
                        self.model.Add( 
                            sum( 
                                self.schedule.get((teacher, clss, subject, day, shift), 0) 
                                for day in range(num_days) 
                                for shift in range(num_shifts) 
                            ) 
                            == 0 
                        )

        # 3rd Constraint: Teachers cannot teach more than one subject in a single shift
        for teacher in teachers:
            for day in range(num_days):
                for shift in range(num_shifts):
                    self.model.Add(
                        sum(
                            self.schedule.get((teacher, clss, subject, day, shift), 0)
                            for clss in school_data
                            for subject in school_data[clss]
                        )
                        <= 1
                    )

        # 4th Constraint: Multiple teachers cannot teach a class in the same shift
        for clss in school_data:
            for day in range(num_days):
                for shift in range(num_shifts):
                    self.model.Add(
                        sum(
                            self.schedule.get((teacher, clss, subject, day, shift), 0)
                            for teacher in teachers
                            for subject in school_data[clss]
                        )
                        <= 1
                    )

        # 5th Constraint: The same subject cannot be taught multiple times in one day
        for clss in school_data:
            for subject in school_data[clss]:
                for day in range(num_days):
                    self.model.Add(
                        sum(
                            self.schedule.get((teacher, clss, subject, day, shift), 0)
                            for teacher in teachers
                            for shift in range(num_shifts)
                        )
                        <= 1
                    )


    def solve_schedule(self):
        # Custom Solution Printer to Collect Multiple Schedules
        class MultipleSolutionsCollector(cp_model.CpSolverSolutionCallback):
            def __init__(self, schedule_vars, max_solutions=5):
                cp_model.CpSolverSolutionCallback.__init__(self)
                self._schedule_vars = schedule_vars
                self.solutions = []
                self.solution_count = 0
                self.max_solutions = max_solutions

            def OnSolutionCallback(self):
                if self.solution_count >= self.max_solutions:
                    return # Stop after collecting max_solutions solutions

                solution = []
                for key, var in self._schedule_vars.items():
                    if self.Value(var) == 1:
                        solution.append(key)
                self.solutions.append(solution)
                self.solution_count += 1


        self.solution_collector = MultipleSolutionsCollector(self.schedule)
        self.solver.parameters.enumerate_all_solutions = True
        self.solver.parameters.max_time_in_seconds = 30.0

        status = self.solver.Solve(self.model, self.solution_collector)

        if self.solution_collector.solution_count > 0:
            return "Schedule generated successfully"
        else:
            return "No feasible solution found!"


    def save_schedule_to_csv(self, solutions):
        if not solutions:
            print("No solutions to save.")
            return

        folder_name = "schedules"
        os.makedirs(folder_name, exist_ok=True)
        day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        for i, solution in enumerate(solutions):
            filename = os.path.join(folder_name, f"schedule_{i+1}.csv")
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Day", "Teacher", "Class", "Shift", "Subject"])

                sorted_solution = sorted(solution, key=lambda x: (x[3], x[1], x[2]))  # Sort by day, then class, then shift
                current_day_idx = None

                # Store teacher schedules in a dictionary for later use
                teacher_schedule_data = {}

                for teacher, cls, subject, day, shift in sorted_solution:
                    if day != current_day_idx:
                        current_day_idx = day
                        writer.writerow([day_names[day], teacher, cls, shift, subject])
                    else:
                        writer.writerow(["", teacher, cls, shift, subject])

                    if teacher not in teacher_schedule_data:
                        teacher_schedule_data[teacher] = {}
                    if shift not in teacher_schedule_data[teacher]:
                        teacher_schedule_data[teacher][shift] = {}
                    teacher_schedule_data[teacher][shift][day_names[day]] = (cls, subject)

            # Create a separate teacher-wise schedule file
            teacher_filename = os.path.join(folder_name, f"teacher_schedule_{i + 1}.csv")
            with open(teacher_filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                header = ["Teacher"] + [f"Shift {i}" for i in range(num_shifts)]
                writer.writerow(header)


                sorted_teachers = sorted(teacher_schedule_data.keys())

                for teacher in sorted_teachers:
                    teacher_row = [teacher]
                    for shift in range(num_shifts):
                        shift_schedule_list = []
                        if teacher in teacher_schedule_data and shift in teacher_schedule_data[teacher]:
                            for day_name in day_names:
                                if day_name in teacher_schedule_data[teacher][shift]:
                                    cls, subject = teacher_schedule_data[teacher][shift][day_name]
                                    shift_schedule_list.append(f"{day_name}: {cls}-{subject}")
                        shift_schedule_text = "\n".join(shift_schedule_list)  # Join days for better readability
                        teacher_row.append(shift_schedule_text)
                    writer.writerow(teacher_row)


    def generate_schedule(self): # Modified generate_schedule to orchestrate and return status
        self.build_model() # Build the model first
        status_message = self.solve_schedule() # Solve and get status message
        if status_message == "Schedule generated successfully":
            self.save_schedule_to_csv(self.solution_collector.solutions) # Save if successful
            return status_message
        else:
            return status_message