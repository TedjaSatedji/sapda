import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
USERNAME = os.getenv("SPADA_USERNAME")
PASSWORD = os.getenv("SPADA_PASSWORD")

# Telegram Bot

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

# Load schedule
def load_schedule(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

# Find current class
def get_current_class(schedule):
    now = datetime.now()
    day_map = {
        "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
        "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
    }
    today = day_map[now.strftime("%A")]
    current_time = now.strftime("%H:%M")

    for entry in schedule:
        if entry["Day"] == today:
            start_time, end_time = entry["Time"].split(" - ")
            if start_time <= current_time <= end_time:
                return entry["CourseName"]
    return None

# Launch browser
def init_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    return webdriver.Chrome(options=options)

# Main automation
def login_and_attend(course_name):
    driver = init_driver()
    driver.get("https://spada.upnyk.ac.id/login/index.php")
    
    # Login
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "loginbtn").click()
    time.sleep(4)

    # Search for course
    found = False
    courses = driver.find_elements(By.PARTIAL_LINK_TEXT, course_name)
    for course in courses:
        if course_name.lower() in course.text.lower():
            course.click()
            found = True
            break
    
    if not found:
        print("Course not found.")
        driver.quit()
        return

    time.sleep(3)

    # Look for 'Presensi' or 'Attendance'
    links = driver.find_elements(By.TAG_NAME, "a")
    attendance_found = False
    for link in links:
        if "presensi" in link.text.lower() or "attendance" in link.text.lower():
            print(f"Found attendance link: {link.text}")
            link.click()
            attendance_found = True
            break

    if not attendance_found:
        print("No attendance link found.")
        send_telegram("No attendance link found.")
        time.sleep(2)
        driver.quit()
        return
        
    
    
    # Submit attendance
    
    attendance_done = False

    try:
        # Try to click the "Submit attendance" link
        driver.find_element(By.PARTIAL_LINK_TEXT, "Submit attendance").click()
        time.sleep(2)

        # Click the "Present" radio button
        labels = driver.find_elements(By.CSS_SELECTOR, "label.form-check-label")

        for label in labels:
            try:
                span = label.find_element(By.CLASS_NAME, "statusdesc")
                if span.text.strip().lower() == "present":
                    radio = label.find_element(By.TAG_NAME, "input")
                    radio.click()
                    break
            except Exception as e:
                continue  # Skip labels that don't match structure

        # Click the save/submit button
        driver.find_element(By.ID, "id_submitbutton").click()

        print("✅ Attendance submitted!")
        send_telegram("✅ Attendance submitted successfully.")
        attendance_done = True

    except Exception as e:
        print("⚠️ Could not submit attendance:", e)

    # Handle notification if it wasn't done
    if not attendance_done:
        print("❌ No attendance available.")
        send_telegram("❌ No attendance available.")

    driver.quit()
        

# Run everything
schedule = load_schedule("schedule.csv")
current_class = get_current_class(schedule)

if current_class:
    print(f"Current class: {current_class}")
    login_and_attend(current_class)
else:
    print("No class at the moment.")
    send_telegram("No class at the moment!.")
