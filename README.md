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

### 2. Add Your Schedule

1. Create a CSV file (e.g., `schedule.csv`) with the following format:

    | CourseName                           | Day    | Time           |
    |--------------------------------------|--------|----------------|
    | Pendidikan Kewarganegaraan           | Rabu   | 09:30 - 11:15  |
    | Technopreneurship                    | Jumat  | 07:00 - 09:30  |
    | Analisa Algoritma                    | Senin  | 10:00 - 11:45  |
    | Otomata Dan Pengantar Kompilasi      | Rabu   | 12:00 - 14:30  |

    **CSV Example:**
    ```csv
    CourseName,Day,Time
    Pendidikan Kewarganegaraan,Rabu,09:30 - 11:15
    Technopreneurship,Jumat,07:00 - 09:30
    Analisa Algoritma,Senin,10:00 - 11:45
    Otomata Dan Pengantar Kompilasi,Rabu,12:00 - 14:30
    ```

2. Place the CSV file in the root folder of the project.

---

**Note:**  
This project is still under development. Contributions and feedback are welcome!
