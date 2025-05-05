import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def make_todo(on, off):
    global test
    test = tk.BooleanVar(value=False)

    body_frame_test = tk.LabelFrame(body_frame, height=50, width=350, padx=15, pady=10)
    body_frame_test.pack()
    body_frame_test.pack_propagate(False)
    body_frame_test.grid_propagate(False)

    checkbox_test = ttk.Checkbutton(body_frame_test, onvalue=True, offvalue=False, variable=test, command=idk)
    checkbox_test.grid(row=0, column=0)

    label_test = ttk.Label(body_frame_test, width=30, text=add_text.get())
    label_test.grid(row=0, column=1, padx=10, pady=5)

    delete_button_test = ttk.Button(body_frame_test, text="Delete", width=7)
    delete_button_test.grid(row=0, column=2, pady=5)

def idk():
    print("hello")

main_frame = tk.LabelFrame(root, height=500, width=400, padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

title_frame = tk.LabelFrame(main_frame, height=55, width=350)
title_frame.pack()
title_frame.pack_propagate(False)

title = ttk.Label(title_frame, text="To-Do List", font=("Arial", 18))
title.pack(pady=10)

body_frame = tk.LabelFrame(main_frame, height=350, width=350, padx=15, pady=10)
body_frame.pack()
body_frame.pack_propagate(False)
body_frame.grid_propagate(False)

List_widget = tk.Listbox(body_frame, height=10, width=50)
List_widget.grid(row=0, column=0, padx=10, pady=5)

List_widget.insert(2, "Sample Item 1")
List_widget.insert(1, "Sample Item 12")

#User Entry Interface
add_frame = tk.LabelFrame(main_frame, height=50, width=350, padx=65)
add_frame.pack()
add_frame.pack_propagate(False)
add_frame.grid_propagate(False)

add_text = ttk.Entry(add_frame)
add_text.grid(row=0, column=0, pady=10, sticky="e")

add_button = ttk.Button(add_frame, text="+", command=lambda:make_todo(1,2))
add_button.grid(row=0, column=1, pady=10, sticky="e")

root.mainloop()