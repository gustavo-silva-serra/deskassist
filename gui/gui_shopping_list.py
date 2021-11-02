import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def cross_item(event, from_tree, to_tree, cross_item_method):
    for selected_item in from_tree.selection():
        item = from_tree.item(selected_item)
        record = item['values']
        if messagebox.askokcancel('', f'Riscar {record}'):
            cross_item_method('', selected_item, True)
            from_tree.delete(selected_item)
            insert_sorted(to_tree, selected_item, item['values'][0])

def add_item(event, from_tree, to_tree, cross_item_method):
    for selected_item in from_tree.selection():
        item = from_tree.item(selected_item)
        cross_item_method('', selected_item, False)
        from_tree.delete(selected_item)
        insert_sorted(to_tree, selected_item, item['values'][0])

def create_treeview(root, title, items, col):
    tree = ttk.Treeview(root, columns=('item'), show='headings', style='big.Treeview', padding=(5,5,5,0))
    tree.heading('item', text=title)
    
    for item in items:
        insert_sorted(tree, item['id'], item['value'])
    
    tree.grid(row=0, column=col, sticky='nsew')

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=col + 1, sticky='ns')
    root.grid_columnconfigure(col, weight=1)

    return tree

def add_handler(from_tree, to_tree, handler, cross_item_method):
    def inner_handler(event):
        handler(event, from_tree, to_tree, cross_item_method)
    from_tree.bind('<<TreeviewSelect>>', inner_handler)

def insert_sorted(tree, new_id, value):
    value = value.lower()
    for iid in tree.get_children():
        if (value < tree.item(iid)['values'][0]):
            tree.insert('', tree.index(iid), iid=new_id, values=[value])
            return
    tree.insert('', tk.END, iid=new_id, values=[value])

def draw_shopping_list_frame(container, items, cross_item_method):
    frame = ttk.Frame(container, borderwidth=3)
    frame.pack(fill='both', expand=True)
    
    tree_nc = create_treeview(frame, 'Comprar', items[0], 0)
    tree_cr = create_treeview(frame, 'Anteriores', items[1], 2)

    s = ttk.Style()
    s.configure('big.Treeview', font=('Consolas', 11))

    add_handler(tree_nc, tree_cr, cross_item, cross_item_method)
    add_handler(tree_cr, tree_nc, add_item, cross_item_method)
    
    frame.grid_rowconfigure(0, weight=1)

    return frame