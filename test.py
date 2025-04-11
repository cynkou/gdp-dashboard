import streamlit as st
import numpy as np
import tempfile
import scipy.io.wavfile
import base64
import matplotlib.pyplot as plt
from io import BytesIO
from pydub import AudioSegment

# --------------------------------------------------------
# SIMPLIFIED MUSIC APP + AUDIO UPLOAD
# --------------------------------------------------------

######################## PART ONE  ########################
# Simple Note Frequencies [C major scale & basics only]
NOTE_FREQUENCIES = {
    "C4": 261.63, "D4": 293.66, "E4": 329.63,
    "F4": 349.23, "G4": 392.00, "A4": 440.00, "B4": 493.88,
    "C5": 523.25,
    "C3": 130.81, "E3": 164.81, "G3": 196.00, "A3": 220.00, "B3": 246.94
}

def generate_sine_wave(freq, duration=0.5, rate=44100):
    t = np.linspace(0, duration, int(rate * duration), False)
    return 0.5 * np.sin(2 * np.pi * freq * t)

def generate_silence(duration=0.3, rate=44100):
    return np.zeros(int(rate * duration))

def save_wave(note_array, rate=44100):
    audio = np.int16(note_array / np.max(np.abs(note_array)) * 32767)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    scipy.io.wavfile.write(temp_file.name, rate, audio)
    return temp_file.name

def get_binary_download_link(file_path, label="Download sound"):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:audio/wav;base64,{b64}" download="my_music.wav">{label}</a>'

def part_one_ui():
    st.title("🎵 Simple Music Player & Audio Visualizer")
    st.markdown("""
    Type **one note** or a **chord** (with `+`) per line.

    **Examples:**
    - `C4`
    - `C4+E4+G4`
    - `G3+B3+D4`
    """)
    music_input = st.text_area("Your Notes/Chords Here:", height=200, value="C4+E4+G4\nF4+A4+C5\nG3+B3+D4")
    duration = st.slider("Duration per line (seconds)", 0.5, 3.0, 2.0, 0.1)
    total_lines = len(music_input.strip().split("\n"))
    total_time = round(total_lines * (duration + 0.3), 2)
    st.markdown(f"Estimated Total Play Time: **{total_time} seconds**")
    return music_input, duration


######################## MAIN CALL  ##########################################
def main():
    music_input, duration = part_one_ui()
  

if __name__ == "__main__":
    main()
