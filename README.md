# Automatic Attendance Script (Work in Progress)

Easily automate your attendance process with this selenium script.

---

## Getting Started

### 1. Install Dependencies

1. Install the dependencies using pip:
    ```sh
    pip install -r requirements.txt
    ```

---

### 2. Add Your Credentials

1. Create a new `.env` file in the project root.
2. Add the following variables:
    ```env
    SPADA_USERNAME=your_username
    SPADA_PASSWORD=your_password
    TELEGRAM_TOKEN=your_telegram_bot_token
    TELEGRAM_CHAT_ID=your_telegram_chat_id
    ```

---

### 3. Add Your Schedule

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

2. Place the CSV file in the root folder of the project.

---

### 4. Telegram Notifications

This script can send notifications to your Telegram account using a bot.  
To enable this:

1. [Create a Telegram bot](https://core.telegram.org/bots#6-botfather) and get the bot token.
2. Get your chat ID (you can use [@userinfobot](https://t.me/userinfobot) on Telegram).
3. Add `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` to your `.env` file as shown above.
4. The script will send messages for attendance status and errors.

---

**Note:**  
This project is still under development. Contributions and feedback are welcome!
