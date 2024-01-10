import requests
import tkinter as tk 
from PIL import Image, ImageTk

def buscar_doguinho(): 
  url = 'https://dog.ceo/api/breeds/image/random'
  response  = requests.get(url)
  dados  =  response.json()
  image_url  =  dados['message']

response_imagem =  requests.url(image_url)
image_bytes = io.BytesIO(response_imagem.content)
image_pillow = Image.open(image_bytes)
image_pillow.thumbnail((400,400))

image_tk = ImageTk.PhotoImage(image_pillow)
image_label.config(image = image_tk)
image_label.image  =  image_tk



root =  tk.Tk()


root.mainloop()
