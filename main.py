import pyautogui
import pyperclip
import pandas as pd
import time

#===This is my settings EB===
delay_between_fields = 0.35
start_delay = 4.5
csv_file = 'form_data.csv'

#===This loads the data EB===
data = pd.read_csv(csv_file)
row = data.iloc[0] #for now it only gets the first row EB

fields = [row['Name'], row['Email'], row['Message']]

#===This is the start delay EB===
print(f"Move your mouse to the first field for Fill to fill the form! Starting in {start_delay} seconds...")
time.sleep(start_delay)

#===INPUT LOOP EB===
for field in fields:
    pyperclip.copy(str(field)) #copy the field to the clipboard EB
    pyautogui.hotkey('ctrl', 'v') #paste the field into the field EB
    pyautogui.press('tab') #move to the next field EB
    time.sleep(delay_between_fields) #wait a bit before moving between fields EB
    
    print("Fill filled the field!")
