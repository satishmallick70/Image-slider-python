from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

# Initialize Tkinter window
rootWindow = tk.Tk()
rootWindow.title("Image Slider")

# List of image paths (fixed comma placement)
image_paths = [
    r"/Users/satishkumar/Desktop/Screenshot 2025-02-08 at 9.33.15 AM.png",
    r"/Users/satishkumar/Desktop/Screenshot 2025-02-08 at 9.33.31 AM.png",
    r"/Users/satishkumar/Desktop/Screenshot 2025-02-09 at 12.22.16 AM.png",
    r"/Users/satishkumar/Desktop/Screenshot 2025-02-09 at 12.25.08 AM.png"
]

# Resize the images
image_size = (500, 500)  # Adjust size as needed
images = [Image.open(path).resize(image_size) for path in image_paths]  # ✅ Fixed Here

# Convert images to Tkinter format
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Tkinter label to display images
label = tk.Label(rootWindow)
label.pack()

# Iterator to cycle through images
slideshow = cycle(photo_images)

def update_image():
    """Update the label with the next image in the cycle."""
    next_image = next(slideshow)
    label.config(image=next_image)
    label.image = next_image  # Keep a reference
    rootWindow.after(2000, update_image)  # Change image every 2 seconds

# Button to start slideshow
play_button = tk.Button(rootWindow, text="Play", command=update_image)
play_button.pack()

# Start Tkinter event loop
rootWindow.mainloop()
