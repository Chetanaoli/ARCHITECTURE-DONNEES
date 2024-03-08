import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import easyocr

def extract_text_from_image(image_path, language='en'):
    reader = easyocr.Reader([language])
    result = reader.readtext(image_path)
    extracted_text = ""
    for detection in result:
        text = detection[1]
        extracted_text += text + " "
    return extracted_text.strip()

def load_image():
    global photo
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        extracted_text = extract_text_from_image(file_path)
        answer_label.config(text=f"Answer: {extracted_text}")

# Create the main window
root = tk.Tk()
root.title("Image Text Extraction")

# Create widgets
load_button = tk.Button(root, text="Load Image", command=load_image)
image_label = tk.Label(root)
answer_label = tk.Label(root, text="Answer: ")

# Organize widgets using grid layout
load_button.grid(row=0, column=0, pady=10)
image_label.grid(row=1, column=0, pady=10)
answer_label.grid(row=2, column=0, pady=10)

# Start the main loop
root.mainloop()
