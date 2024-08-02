import tkinter as tk
from tkinter import ttk
from gui import create_main_window
from tts import initialize_tts
import torch
import threading

device = "cuda" if torch.cuda.is_available() else "cpu"

def initialize_tts_in_background(root, loading_window, loading_text, main_window):
    def target():
        loading_text.insert(tk.END, "Loading TTS model...\n")
        root.update_idletasks()
        initialize_tts(root, device, loading_text)
        loading_text.insert(tk.END, "TTS model loaded.\n")
        root.update_idletasks()
        loading_window.destroy()
        main_window.deiconify()
    
    threading.Thread(target=target).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window initially

    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    loading_text = tk.Text(loading_window, height=1, width=50)
    loading_text.pack(pady=10)
    loading_text.insert(tk.END, "Loading TTS model...")

    main_window = tk.Toplevel(root)
    main_window.title("Text and Image Input")
    main_window.withdraw()  # Hide the main window until the model is loaded

    loading_text, text_area, dropdown, image_label = create_main_window(main_window, device)
    initialize_tts_in_background(root, loading_window, loading_text, main_window)

    root.mainloop()