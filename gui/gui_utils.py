import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def load_img(fname, size):
    '''
        Carrega uma imagem nomeada por fname, redimensionado para size x size

    ---
    Retorna um ImageTk.PhotoImage contendo a imagem
    '''
    img = Image.open(fname)
    img = img.resize((size,size), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def load_img_as_lbl(container, fname, size):
    '''
        Carrega uma imagem nomeada por fname, redimensionado para size x size

    ---
    Retorna um Label contendo a imagem
    '''
    img = load_img(fname, size)
    lbl = ttk.Label(container, image=img)
    lbl.image = img
    return lbl