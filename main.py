import pyautogui
import pyperclip
import pandas as pd
import time

#===This is my settings===
delay_between_fields = 1
start_delay = 5
csv_file = 'form_data.csv'

#===This loads the data===
data = pd.read_csv(csv_file)
row = data.iloc[0] #for now it only gets the first row

fields = [row['Name'], row['Email'], row['Message']]

#===This is the start delay===
print(f"Move your mouse to the first field! Starting in {start_delay} seconds...")
time.sleep(start_delay)

#===INPUT LOOP===
for field in fields:
    pyperclip.copy(str(field)) #copy the field to the clipboard
    pyautogui.hotkey('ctrl', 'v') #paste the field into the field
    pyautogui.press('tab') #move to the next field
    time.sleep(delay_between_fields) #wait a bit before moving between fields
    
    print("Form filled successfully!")
