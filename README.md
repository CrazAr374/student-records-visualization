# Student Records Visualization

This project is a Python-based CLI application that allows you to manage student records, display the data in a tabular format, and visualize student marks using a bar chart.

## Features:
- **Add Student:** Allows users to add a student's roll number, name, marks obtained, and remarks.
- **Display Table:** Shows the list of all students and their details in a neat, tabular format.
- **Plot Marks:** Visualizes students' marks in the form of a bar chart.
- **Exit:** Option to exit the application.

## Technologies Used:
- **Python 3.x**
- **matplotlib**: For visualizing marks in a bar chart.
- **tabulate**: For displaying student data in a tabular format.

## Requirements:
- Python 3.x
- Install dependencies by running:
  ```bash
  pip install matplotlib tabulate
  ```

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-records-visualization.git
   ```
2. Navigate to the project directory:
   ```bash
   cd student-records-visualization
   ```
3. Run the script:
   ```bash
   python student_records.py
   ```

## Features in Detail:

### 1. Add Student
This option allows you to add a new student's details (roll number, name, marks obtained, and remarks). Each student's information is stored in a list.

### 2. Display Table
This option prints the current list of students in a table format using the `tabulate` library.

### 3. Plot Marks
This option generates a bar chart using `matplotlib` to display the marks obtained by each student, indexed by their roll number.

### 4. Exit
Select this option to exit the program.

## Example:

### Sample Table Display:
```
+---------------+----------+----------------+-----------+
| Roll Number   | Name     | Marks Obtained | Remarks   |
+---------------+----------+----------------+-----------+
| 1             | John Doe | 85             | Good      |
| 2             | Jane Roe | 78             | Average   |
+---------------+----------+----------------+-----------+
```

### Sample Bar Chart:
![Bar Chart](./sample_bar_chart.png)

## Contributing:
Feel free to fork the repository and submit pull requests.
