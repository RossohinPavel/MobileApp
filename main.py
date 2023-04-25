import tkinter as tk


root = tk.Tk()

result_listbox = tk.Listbox(root)
listbox_vars = []


def show_result_frame():
    result_listbox.pack(expand=1, fill=tk.X)
    minus_button = tk.Button(root, text='–', width=4, font='arial 12 bold')
    minus_button.pack(anchor=tk.E)


def show_work_frame(lbl, side):
    frame = tk.Frame(root)
    label = tk.Label(frame, text=lbl)
    label.pack(expand=1, fill=tk.X)
    list_box = tk.Listbox(frame)
    listbox_vars.append(list_box)
    list_box.pack(expand=1, fill=tk.X)
    button_frame = tk.Frame(frame)
    button_frame.pack(expand=1, fill=tk.X)
    plus_button = tk.Button(button_frame, text='+', width=4, font='arial 12 bold', command=None)
    plus_button.pack(side=tk.LEFT, expand=1, fill=tk.X)
    minus_button = tk.Button(button_frame, text='–', width=4, font='arial 12 bold', command=None)
    minus_button.pack(side=tk.RIGHT, expand=1, fill=tk.X)
    frame.pack(side=side, expand=1, fill=tk.X)


if __name__ == '__main__':
    show_result_frame()
    show_work_frame('Обложки', tk.LEFT)
    show_work_frame('Развороты', tk.RIGHT)
    root.mainloop()
