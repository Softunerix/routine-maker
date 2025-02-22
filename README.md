# Routine Maker

## Introduction

This Routine Maker is designed to automate the process of creating class schedules, specifically for Bangladeshi schools. It aims to simplify the often complex and time-consuming task of manual routine creation by leveraging constraint satisfaction problem (CSP) solving techniques. The tool is built with a user-friendly graphical interface (GUI) and is tailored to accommodate the typical constraints and requirements of schools in Bangladesh.

## Key Features

*   **User-Friendly GUI:** Built with Tkinter, providing an intuitive interface to manage classes, subjects, and teachers.
*   **Class Management:**  Easily add and manage class names.
*   **Subject Management:** Add subjects to classes, specifying the required number of days per week for each subject.
*   **Teacher Management:** Add teacher names to the system.
*   **Teacher-Class-Subject Assignment:**  Define which teachers can teach which subjects in specific classes.
*   **Shift Management:** Configure the number of shifts (periods) per day in the school schedule.
*   **Schedule Generation:** Automatically generates multiple feasible school routines based on defined constraints.
*   **Output to CSV:** Saves generated schedules in CSV format for easy viewing and distribution.
*   **Teacher-wise Schedule Output:**  Generates separate CSV files showing individual teacher schedules for better organization.
*   **Constraint-Based Scheduling:** Utilizes constraint programming to ensure schedules are valid and adhere to school requirements (e.g., teachers not double-booked, subjects taught required days, etc.).

## Getting Started

### Prerequisites

*   **Python 3.x:**  Ensure you have Python 3 or a later version installed on your system.
*   **OR-Tools Library:** Install Google OR-Tools for constraint programming. You can install it using pip:
    ```bash
    pip install ortools
    ```
*   **Tkinter:**  Tkinter is usually included with standard Python installations. If not, you might need to install it separately based on your operating system (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu).

### Installation

1.  **Clone the Repository:**  `git clone https://github.com/Softunerix/routine-maker.git`

### Running the Application

1.  **Execute `main.py`:** Run the GUI application by executing the following command in your terminal:
    ```bash
    python main.py
    ```
2.  **Using the GUI:** The "School Routine Management System" window will appear. Use the buttons to:
    *   **Add Class:**  Add new classes to the system (e.g., "Class 6", "Class 7").
    *   **Add Subject:** Add subjects to specific classes and define the number of days per week they should be taught (e.g., "Math" for "Class 6" - 6 days).
    *   **Add Teacher:** Add teachers to the system (e.g., "Mr. Rahim", "Ms. Fatima").
    *   **Add Class to Teacher:** Assign classes to teachers.
    *   **Add Subject to Teacher for Class:** Specify which subjects a teacher can teach in a particular class.
    *   **Set Number of Shifts:** Define the number of teaching periods (shifts) in a school day.
    *   **Show Classes:** View the list of classes and subjects.
    *   **Show Teachers:** View the list of teachers.
    *   **Generate Schedule:**  Initiate the schedule generation process. The generated schedules will be saved as CSV files in a "schedules" folder.

## Project Structure

*   **`gui.py`:** Contains the main Tkinter GUI application code. Handles user interactions, button events, and calls functions from other modules.
*   **`school_data_management.py`:**  Manages school data (classes, subjects, teachers, schedules). Includes functions for adding classes, subjects, teachers, and related data.
*   **`constraint.py`:**  Houses the `scheduleMaker` class. This class implements the constraint programming model using OR-Tools to generate school schedules based on the defined data and constraints.
*   **`UI directory`:** Contains UI components like `ClassesWindow`, `TeachersWindow` for displaying data in separate windows, keeping `gui.py` cleaner.
*   **`schedules/` folder:**  (Created upon schedule generation) Stores the generated schedules as CSV files.

## Dependencies

*   **Python Standard Library:** (Tkinter, csv, os)
*   **OR-Tools:** (For constraint satisfaction solving)

## Future Plans and Potential Improvements

This Routine Maker is a work in progress, and there are many areas for future enhancement:

### Feature Enhancements

*   **More Sophisticated Constraints:**
    *   **Subject Sequencing/Pacing:**  Implement constraints on the order or distribution of subjects throughout the week (e.g., avoid back-to-back heavy subjects).
    *   **Break Times/Lunch Breaks:**  Integrate break times and lunch periods into the schedule.
    *   **Resource Allocation:**  Manage resources like labs, libraries, or equipment.
*   **Schedule Optimization:**
    *   **Prioritize Teacher Preferences:** Optimize schedules to maximize teacher satisfaction based on preferences.
    *   **Balance Workload:**  Distribute workload more evenly among teachers.
*   **Advanced Reporting and Visualization:**
    *   **Schedule Reports:** Generate detailed reports summarizing schedule statistics, teacher workload, etc.
    *   **Visual Schedule Representation:** Display schedules in a more visually appealing format (e.g., weekly timetable view in the GUI).
    *   **Calendar Integration:**  Export schedules to calendar applications (e.g., Google Calendar).
*   **User Roles and Permissions:** Implement user roles (administrator, teacher) with different levels of access and functionality.
*   **Database Integration:**  Store school data and schedules in a database (e.g., SQLite, PostgreSQL) for persistence and scalability.
*   **Web-Based Interface:**  Develop a web interface using frameworks like Flask or Django to make the Routine Maker accessible over a network and to a wider range of users.
*   **Import/Export Data:**  Allow importing data from existing school management systems and exporting schedules in various formats.

### Potential Errors and Error Handling Improvements

*   **Input Validation:**
    *   **Data Type Validation:** Implement stricter input validation in the GUI to ensure that users enter correct data types (e.g., numbers for days, valid class/subject/teacher names).
    *   **Empty Field Checks:** Prevent users from submitting forms with empty required fields.
    *   **Range Checks:** Validate that input values are within acceptable ranges (e.g., days per week should be a positive number within a reasonable limit).
*   **Constraint Satisfaction Issues:**
    *   **"No Feasible Solution" Handling:**  Improve the handling of cases where no feasible schedule can be generated due to over-constrained data. Provide more informative error messages to the user, suggesting ways to relax constraints or adjust data.
    *   **Over-Constrained Scenarios:**  Implement mechanisms to detect and diagnose over-constrained scenarios, potentially suggesting which constraints are conflicting.

*   **User Interface Improvements:**
    *   **Clearer Error Messages:** Display user-friendly and informative error messages in the GUI instead of just console outputs or generic error dialogs.
    *   **Progress Indicators:**  Add progress bars or loading indicators during schedule generation, which can be time-consuming.

**Key Future Constraint Enhancements:**

*   **Integration of Teacher's Assistants (TA Option):**
    *   Future versions of the Routine Maker will introduce the ability to incorporate **Teacher's Assistants (TAs)** into the scheduling process. This enhancement will enable schools to:
        *   **Assign TAs to specific classes:**  Allowing for the allocation of Teacher's Assistants to support lead teachers in classrooms, particularly in larger classes or for subjects requiring additional instructional support.
        *   **Define TA Availability and Roles:**  Implement mechanisms to specify TA availability, preferred class assignments, and potentially define different roles or responsibilities for TAs within the scheduling model.
        *   **Optimize TA Utilization:**  Enhance schedule generation to effectively utilize Teacher's Assistants to improve student support, manage classroom workload, and optimize teacher-to-student ratios where appropriate.

*   **Advanced Dual-Teacher Classroom Support:**
    *   Building upon the planned feature for dual-teacher classrooms, future development will further refine and expand this functionality.  We aim to provide robust options for:
        *   **Flexible Teacher Pairing:**  Enhancements to allow for more nuanced teacher pairing logic based on teacher expertise, subject specialization, teaching styles, or desired co-teaching methodologies.
        *   **Student Group Management in Dual-Teacher Classes:**  Improved features for managing student groupings within dual-teacher classes, facilitating scenarios where students are deliberately divided for specific instructional purposes or parts of the subject curriculum.
        *   **Constraint-Aware Dual-Teacher Scheduling:**  Refining the constraint model to fully account for the complexities of dual-teacher assignments, ensuring efficient resource allocation and schedule feasibility even with increased teacher assignments per class.

## License

This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

[![Apache-2.0 license badge](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Acknowledgments

Thanks to Gemini for assistance.
