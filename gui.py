import tkinter as tk
from tkinter import ttk
from image import upload_image
from tts import generate_voice

def create_main_window(root, device):
    global dropdown
    cuda_status = tk.Text(root, height=1, width=50)
    cuda_status.pack(pady=10)
    cuda_status.insert(tk.END, f"CUDA MODE {'GPU' if device == 'cuda' else 'CPU'}")

    global text_area
    text_area = tk.Text(root, height=10, width=50)
    text_area.pack(pady=10)

    generate_voice_button = tk.Button(root, text="Generate Voice", command=lambda: generate_voice(text_area, dropdown))
    generate_voice_button.pack(pady=10)

    upload_button = tk.Button(root, text="Upload Image", command=upload_image)
    upload_button.pack(pady=10)

   

    global image_label
    image_label = tk.Label(root)
    image_label.pack(pady=10)

    global loading_text
    loading_text = tk.Text(root, height=1, width=50)
    loading_text.pack(pady=10)
    loading_text.insert(tk.END, "Loading TTS model...")

    values = ['Claribel Dervla', 'Daisy Studious', 'Gracie Wise', 'Tammie Ema', 'Alison Dietlinde', 
              'Ana Florence', 'Annmarie Nele', 'Asya Anara', 'Brenda Stern', 'Gitta Nikolina', 
              'Henriette Usha', 'Sofia Hellen', 'Tammy Grit', 'Tanja Adelina', 'Vjollca Johnnie', 
              'Andrew Chipper', 'Badr Odhiambo', 'Dionisio Schuyler', 'Royston Min', 'Viktor Eka', 
              'Abrahan Mack', 'Adde Michal', 'Baldur Sanjin', 'Craig Gutsy', 'Damien Black', 
              'Gilberto Mathias', 'Ilkin Urbano', 'Kazuhiko Atallah', 'Ludvig Milivoj', 'Suad Qasim', 
              'Torcull Diarmuid', 'Viktor Menelaos', 'Zacharie Aimilios', 'Nova Hogarth', 'Maja Ruoho', 
              'Uta Obando', 'Lidiya Szekeres', 'Chandra MacFarland', 'Szofi Granger', 'Camilla Holmström', 
              'Lilya Stainthorpe', 'Zofija Kendrick', 'Narelle Moon', 'Barbora MacLean', 'Alexandra Hisakawa', 
              'Alma María', 'Rosemary Okafor', 'Ige Behringer', 'Filip Traverse', 'Damjan Chapman', 
              'Wulf Carlevaro', 'Aaron Dreschner', 'Kumar Dahl', 'Eugenio Mataracı', 'Ferran Simen', 
              'Xavier Hayasaka', 'Luis Moray', 'Marcos Rudaski']


    dropdown = ttk.Combobox(root, values=values)
    dropdown.pack(pady=10)

    return loading_text, text_area, dropdown, image_label