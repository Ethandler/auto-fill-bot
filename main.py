import pyautogui
import pyperclip
import pandas as pd
import time

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

# === Load Data ===
data = pd.read_csv(csv_file)
row = data.iloc[0]

# === Helper Functions ===
def paste_field(text):
    pyperclip.copy(str(text))
    time.sleep(delay_between_fields)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(delay_between_fields)
    pyautogui.press('tab')

def click_dropdown_and_select(x, y, option_map, option_name):
    pyautogui.click(x, y)
    time.sleep(0.2)
    presses = option_map.get(option_name, 0)
    pyautogui.press('down', presses=presses, interval=0.1)
    pyautogui.press('enter')
    time.sleep(delay_between_fields)
    pyautogui.press('tab')

def check_contact_method(method):
    tab_moves = contact_checkbox_tab_counts.get(method, 0)
    for _ in range(tab_moves):
        pyautogui.press('tab')
        time.sleep(0.1)
    pyautogui.press('space')  # Check the box
    time.sleep(delay_between_fields)
    pyautogui.press('tab')  # Move to next input

# === Start Automation ===
print(f"Move mouse to the first field. Starting in {start_delay} seconds...")
time.sleep(start_delay)

# === Auto-fill Standard Fields ===
paste_field(row['First Name'])
paste_field(row['Last Name'])
paste_field(row['Email'])
paste_field(row['Street Address'])
paste_field(row['Street Address Line 2'])
paste_field(row['City'])

# === Dropdown: State ===
click_dropdown_and_select(404, 462, state_dropdown, row['State / Province'])

paste_field(row['Postal / Zip Code'])
paste_field(row['Phone Number'])

# === Dropdown: Service Type ===
click_dropdown_and_select(232, 581, service_dropdown, row['Service Type'])

# === Checkbox: Contact Via (Email / Phone / Text) ===
check_contact_method(row['Contact Via'])

# === Final Text Area ===
paste_field(row['Type a Question'])

print("✅ All fields filled by Fill!")
