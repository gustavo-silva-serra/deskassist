import tkinter as tk
from tkinter import ttk
from gui import gui_previsao
from forecast.cptec_forecast import CptecWeather

current = CptecWeather.current()
next_days = CptecWeather.next_days()

# root window
root = tk.Tk()
#root.geometry('500x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill='both', expand=True)

# create frames

frame2 = ttk.Frame(notebook)
frame2.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(gui_previsao.draw_forecast_frame(notebook, current, next_days[0], next_days[1]), text='Previsão')
notebook.add(frame2, text='Mercado')

root.mainloop()
