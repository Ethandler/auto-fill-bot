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
state_dropdown = {
    "Select State": 0,
    "Arizona": 1,
    "California": 2,
    "Texas": 3,
    "New York": 4
}

service_dropdown = {
    "Select Service": 0,
    "Consultation": 1,
    "Repair": 2,
    "Installation": 3,
    "Other": 4
}

contact_checkbox_tab_counts = {
    "Email": 0,
    "Phone": 1,
    "Text": 2
}

# === Image File Names ===
STATE_DROPDOWN_IMG = 'dropdown_state.png'
SERVICE_DROPDOWN_IMG = 'dropdown_service.png'

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
        location = pyautogui.locateCenterOnScreen("Screenshot 2025-04-11 110229.png", confidence=0.8)
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

paste_field(row['First Name'])
paste_field(row['Last Name'])
paste_field(row['Email'])
paste_field(row['Street Address'])
paste_field(row.get('Street Address Line 2', ''))  # Optional
paste_field(row['City'])

click_dropdown_by_image(STATE_DROPDOWN_IMG, state_dropdown, row['State / Province'], label="State")
paste_field(row['Postal / Zip Code'])
paste_field(row['Phone Number'])

click_dropdown_by_image(SERVICE_DROPDOWN_IMG, service_dropdown, row['Service Type'], label="Service Type")
check_contact_method(row['Contact Via'])

paste_field(row['Type a Question'])

print("✅ All fields filled by FillBot!")
