from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk

def upload_image():
    try:
        file_path = askopenfilename()
        if file_path:
            img = Image.open(file_path)
            
            max_width = 500
            width_percent = (max_width / float(img.size[0]))
            new_height = int((float(img.size[1]) * float(width_percent)))
            
            img = img.resize((max_width, new_height))
            
            img_tk = ImageTk.PhotoImage(img)
            
            image_label.config(image=img_tk)
            image_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        print(f"An error occurred: {e}")
