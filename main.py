import pyautogui
import pyperclip
import pandas as pd
import time


delay_between_fields = 0.65
start_delay = 6.0
csv_file = 'form_data.csv'


data = pd.read_csv(csv_file)
row = data.iloc[0] 

field_names = ['First Name', 'Last Name', 'Email', 'Street Address', 'Street Address Line 2',
               'City', 'State / Province','Postal / Zip Code','Area Code','Phone number','Type a Question',]
fields = []

for name in field_names:
    value = row.get(name, "")  
    fields.append(value)

print("Fields to be entered:", fields)

print(f"Move your mouse to the first field for Fill to fill the form! Starting in {start_delay} seconds...")
time.sleep(start_delay)

#===INPUT LOOP EB===
for field in fields:
    pyperclip.copy(str(field))
    time.sleep(delay_between_fields) 
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(delay_between_fields)  
    pyautogui.press('tab') 
    time.sleep(delay_between_fields) 
    
    print("Fill filled the field!")
