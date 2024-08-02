import torch
from TTS.api import TTS
import numpy as np
import scipy.io.wavfile
from pydub import AudioSegment
from tkinter import messagebox
import tkinter as tk

tts = None

def initialize_tts(root, device, loading_text):
    global tts
    loading_text.insert(tk.END, "Loading TTS model...")
    root.update_idletasks()
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=device == "cuda").to(device)
    loading_text.delete("1.0", tk.END)
    loading_text.insert(tk.END, "TTS model loaded.")

def generate_voice(text_input, dropdown):
    try:
        
        text = text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text.")
            return
        
        selected_speaker = dropdown.get()
        if not selected_speaker:
            messagebox.showwarning("Warning", "Please select a speaker.")
            return
        
        wav = tts.tts(text=text, speaker=selected_speaker, language="de")
        
        if not isinstance(wav, np.ndarray):
            wav = np.array(wav)
        
        audio_data = np.int16(wav * 32767)
        
        wav_file_path = "./hier.wav"
        scipy.io.wavfile.write(wav_file_path, 22050, audio_data)
        
        audio = AudioSegment.from_wav(wav_file_path)
        mp3_file_path = "./hier.mp3"
        audio.export(mp3_file_path, format="mp3")
        
        messagebox.showinfo("Success", "Voice generated and saved successfully as MP3.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        print(f"An error occurred: {e}")