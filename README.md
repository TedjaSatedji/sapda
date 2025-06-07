# Automatic Attendance Script (Work in Progress)

Easily automate your attendance process with this script.

---

## Getting Started

### 1. Add Your Credentials

1. Create a new `.env` file in the project root.
2. Add the following variables:
    ```env
    SPADA_USERNAME=your_username
    SPADA_PASSWORD=your_password
    ```

---

### 2. Add Your Schedule (you cam ask some random llm)

1. Create a CSV file (e.g., `schedule.csv`) with the following format:

    | CourseName                | Day     | Time           |
    |---------------------------|---------|----------------|
    | Data Science Basics       | Senin   | 08:15 - 10:00  |
    | Web Development           | Selasa  | 13:00 - 15:30  |
    | Cloud Computing           | Kamis   | 09:45 - 11:15  |
    | Machine Learning Intro    | Jumat   | 10:30 - 12:00  |

    **CSV Example:**
    ```csv
    CourseName,Day,Time
    Data Science Basics,Senin,08:15 - 10:00
    Web Development,Selasa,13:00 - 15:30
    Cloud Computing,Kamis,09:45 - 11:15
    Machine Learning Intro,Jumat,10:30 - 12:00
    ```
    ```

2. Place the CSV file in the root folder of the project.

---

**Note:**  
This project is still under development. Contributions and feedback are welcome!
