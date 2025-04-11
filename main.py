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

STATE_DROPDOWN_COORDS = (404, 462)
SERVICE_DROPDOWN_COORDS = (232, 581)

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

def click_dropdown_and_select(x, y, option_map, option_name):
    pyautogui.click(x, y)
    time.sleep(0.2)
    presses = option_map.get(option_name, 0)
    for _ in range(presses):
        pyautogui.press('down')
        time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(delay_between_fields)
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

click_dropdown_and_select(*STATE_DROPDOWN_COORDS, state_dropdown, row['State / Province'])
paste_field(row['Postal / Zip Code'])
paste_field(row['Phone Number'])

click_dropdown_and_select(*SERVICE_DROPDOWN_COORDS, service_dropdown, row['Service Type'])
check_contact_method(row['Contact Via'])

paste_field(row['Type a Question'])

print("✅ All fields filled by FillBot!")
