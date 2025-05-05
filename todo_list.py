import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def add_todo():
    if add_text.get() != "":
        List_widget.insert(0, add_text.get())
        add_text.delete(0, tk.END)
    return

def remove_todo():
    List_widget.delete(tk.ANCHOR)
    return

main_frame = tk.LabelFrame(root, height=500, width=400, padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

#Title Frame Widgets with Interactive Widgets
title_frame = tk.LabelFrame(main_frame, height=55, width=350)
title_frame.pack()
title_frame.pack_propagate(False)

title = ttk.Label(title_frame, text="To-Do List", font=("Arial", 18))
title.pack(pady=10)

#Body Frame Widgets
body_frame = tk.LabelFrame(main_frame, height=350, width=350, padx=15, pady=10)
body_frame.pack()
body_frame.pack_propagate(False)
body_frame.grid_propagate(False)

List_widget = tk.Listbox(body_frame, height=19, width=50)
List_widget.pack()

#User Entry Interface
add_frame = tk.LabelFrame(main_frame, height=50, width=350, padx=20, pady=10)
add_frame.pack()
add_frame.pack_propagate(False)
add_frame.grid_propagate(False)

add_frame2 = ttk.Frame(add_frame)
add_frame2.pack()
add_frame2.pack_propagate(False)

add_text = ttk.Entry(add_frame2, width=23)
add_text.grid(row=0, column=0)

add_button = ttk.Button(add_frame2, text="Add", command=lambda:add_todo())
add_button.grid(row=0, column=1)

remove_button = ttk.Button(add_frame2, text="Remove", command=lambda:remove_todo())
remove_button.grid(row=0, column=2)

root.mainloop()