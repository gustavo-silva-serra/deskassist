from tkinter import ttk
from .gui_utils import load_img_as_lbl

def draw_forecast_frame(container, current, tomorrow, after):
    frame = ttk.Frame(container)
    frame.pack(fill='both', expand=True)

    frame.columnconfigure(0, pad=40)
    frame.columnconfigure(1, pad=40)
    frame.columnconfigure(2, pad=40)

    # Monta a exibição do dia atual
    ttk.Label(frame, text='Agora').grid(column=0, row=0)
    load_img_as_lbl(frame, current.icon, 50).grid(column=0, row=1)
    ttk.Label(frame, text=current.text).grid(column=0, row=2)
    ttk.Label(frame, text=f'Temp.:{current.min}°').grid(column=0, row=3)
    #####

    # Monta a exibição do dia de amanhã
    ttk.Label(frame, text='Amanhã').grid(column=1, row=0)
    load_img_as_lbl(frame, tomorrow.icon, 50).grid(column=1, row=1)
    ttk.Label(frame, text=tomorrow.text).grid(column=1, row=2)
    ttk.Label(frame, text=f'Min.:{tomorrow.min}° Máx:{tomorrow.max}°').grid(column=1, row=3)
    #####

    # Monta a exibição do dia depois de amanhã
    ttk.Label(frame, text='Depois').grid(column=2, row=0)
    load_img_as_lbl(frame, after.icon, 50).grid(column=2, row=1)
    ttk.Label(frame, text=after.text).grid(column=2, row=2)
    ttk.Label(frame, text=f'Min.:{after.min}° Máx:{after.max}°').grid(column=2, row=3)
    #####

    return frame