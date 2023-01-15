import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from sklearn.cluster import KMeans
from matplotlib import cm


def top_n_colors(img):
    clt = KMeans(n_clusters=10, n_init=10)
    clt.fit(img.reshape(-1, 3))
    return clt.cluster_centers_


window = tk.Tk()
window.title("Image Colour Palette Generator")
window.minsize(800, 600)

image = Image.open("check_image.jpg")
image_tk = ImageTk.PhotoImage(image.resize((700, 380)))

label = tk.Label(window, image=image_tk)
label.grid(row=0, column=0, columnspan=10)

image = np.asarray(image)

top_10_colors = top_n_colors(image)

top_10_label = tk.Label(window, text="Top 10 most common colors", font=("Arial", 16))
top_10_label.grid(row=1, column=0, columnspan=10)

for i, color in enumerate(top_10_colors):
    color_image = Image.new('RGB', (50, 50), tuple(color.astype(np.uint8)))
    color_tk = ImageTk.PhotoImage(color_image)
    color_label = tk.Label(window, image=color_tk)
    color_label.image = color_tk
    color_label.grid(row=2, column=i)

window.mainloop()
