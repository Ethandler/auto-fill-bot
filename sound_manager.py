# sound_manager.py
import simpleaudio as sa
import random
import os

# Put your sound files in the same folder or a 'sounds' folder
SOUND_FOLDER = "sounds"

click_sound = os.path.join(SOUND_FOLDER, "click.wav")

tab_sounds = [
    os.path.join(SOUND_FOLDER, "tab1.wav"),
    os.path.join(SOUND_FOLDER, "tab2.wav"),
    os.path.join(SOUND_FOLDER, "tab3.wav")
]

def play_click():
    try:
        sa.WaveObject.from_wave_file(click_sound).play()
    except Exception as e:
        print("Click sound error:", e)

def play_random_tab():
    try:
        sound_path = random.choice(tab_sounds)
        sa.WaveObject.from_wave_file(sound_path).play()
    except Exception as e:
        print("Tab sound error:", e)
