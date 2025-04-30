import tkinter as tk
from tkinter import ttk

root = tk.Tk()

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

checkbox_1 = ttk.Checkbutton(body_frame)
checkbox_1.grid(row=0, column=0)

checkbox_2 = ttk.Checkbutton(body_frame)
checkbox_2.grid(row=1, column=0)

checkbox_3 = ttk.Checkbutton(body_frame)
checkbox_3.grid(row=2, column=0)

entry_1 = ttk.Entry(body_frame, width=30)
entry_1.grid(row=0, column=1, padx=10, pady=5)

entry_2 = ttk.Entry(body_frame, width=30)
entry_2.grid(row=1, column=1, padx=10, pady=5)

entry_3 = ttk.Entry(body_frame, width=30)
entry_3.grid(row=2, column=1, padx=10, pady=5)

delete_button_1 = ttk.Button(body_frame, text="Delete")
delete_button_1.grid(row=0, column=2, padx=10, pady=5)

delete_button_2 = ttk.Button(body_frame, text="Delete")
delete_button_2.grid(row=1, column=2, padx=10, pady=5)

delete_button_3 = ttk.Button(body_frame, text="Delete")
delete_button_3.grid(row=2, column=2, padx=10, pady=5)

add_frame = tk.LabelFrame(main_frame, height=50, width=350)
add_frame.pack()
add_frame.pack_propagate(False)

add_button = ttk.Button(add_frame, text="+")
add_button.pack(pady=10)

root.mainloop()