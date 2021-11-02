import tkinter as tk
from tkinter import ttk
from tkinter import font
from gui import gui_previsao
from gui import gui_shopping_list
from shopping_list.shopping_list import ShoppingList
from forecast.cptec_forecast import CptecWeather

current = CptecWeather.current()
next_days = CptecWeather.next_days()
spl = ShoppingList('Shopping List')

exit

# root window
root = tk.Tk()
root.geometry('450x700')
root.title('Desk Assist')

# create frames
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True)

ttk.Label(main_frame, font='Consolas 12', text='Previsão do tempo', background='black', foreground='white', justify='center').pack(fill='x')
gui_previsao.draw_forecast_frame(main_frame, current, next_days[0], next_days[1]).pack(fill='both', expand=False)
ttk.Label(main_frame, font='Consolas 12', text='Mercado', background='black', foreground='white', justify='center').pack(fill='x')
gui_shopping_list.draw_shopping_list_frame(main_frame, spl.get_items(), spl.cross_item).pack(fill='both', expand=False)

root.mainloop()
