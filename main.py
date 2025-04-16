
import pyautogui
import pyperclip
import pandas as pd
import time
import os

# === Settings ===
delay_between_fields = 0.45
start_delay = 6.0
csv_file = 'form_data.csv'

# === Dropdown Option Maps ===
work_type_dropdown = {
    "Select Service": 0,
    "IT Support": 1,
    "Website Development": 2,
    "Software Installation": 3,
    "Consultation": 4
}

priority_dropdown = {
    "Select Priority": 0,
    "Low (1–2 weeks)": 1,
    "Medium (2–3 days)": 2,
    "High (24 hours)": 3
}

contact_checkbox_tab_counts = {
    "Email": 0,
    "Phone": 1,
    "Text": 2
}

# === Image File Names (Full absolute paths) ===
WORK_TYPE_DROPDOWN_IMG = r'D:\Projects\auto-fill-bot\selectservice.png'
PRIORITY_DROPDOWN_IMG = r'D:\Projects\auto-fill-bot\selectpriority.png'

# === Load Data ===
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"❌ CSV file '{csv_file}' not found.")

data = pd.read_csv(csv_file)
if data.empty:
    raise ValueError("❌ CSV file is empty.")

row = data.iloc[0]

# === Helper Functions ===
def paste_field(text):
    try:
        pyperclip.copy(str(text))
        time.sleep(delay_between_fields)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(delay_between_fields)
        pyautogui.press('tab')
    except Exception as e:
        print(f"⚠️ Clipboard Error: {e}")

def click_dropdown_by_image(image_path, option_map, option_name, label="Dropdown"):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location is None:
            raise Exception(f"Image not found: {image_path}")

        pyautogui.click(location)
        time.sleep(0.2)

        presses = option_map.get(option_name.strip(), None)
        if presses is None:
            raise ValueError(f"Unknown option '{option_name}' in {label}")

        for _ in range(presses):
            pyautogui.press('down')
            time.sleep(0.1)

        pyautogui.press('enter')
        time.sleep(delay_between_fields)
        pyautogui.press('tab')

    except Exception as e:
        print(f"⚠️ Dropdown failure in {label}: {e}")
        pyautogui.press('tab')

def check_contact_method(methods):
    for method in str(methods).split(','):
        method = method.strip()
        tab_moves = contact_checkbox_tab_counts.get(method, 0)
        for _ in range(tab_moves):
            pyautogui.press('tab')
            time.sleep(0.1)
        pyautogui.press('space')
        time.sleep(delay_between_fields)
        pyautogui.press('tab')

# === Start Automation ===
print(f"🕹️ Move mouse to the first form field. Starting in {start_delay} seconds...")
time.sleep(start_delay)

paste_field(row['Full Name'])
paste_field(row.get('Business / Company Name', ''))  # Optional
paste_field(row['Email'])
paste_field(row['Phone'])

click_dropdown_by_image(WORK_TYPE_DROPDOWN_IMG, work_type_dropdown, row['Type of Work Needed'], label="Work Type")
click_dropdown_by_image(PRIORITY_DROPDOWN_IMG, priority_dropdown, row['Priority Level'], label="Priority Level")

check_contact_method(row['Preferred Contact Methods'])
paste_field(row['Work Description'])

print("✅ All fields filled by FillBot!")
