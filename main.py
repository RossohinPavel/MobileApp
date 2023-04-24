import tkinter as tk


root = tk.Tk()

result_list = ['test', 'test1']
result_list_var = tk.Variable(root, value=result_list)


def del_result_value():
    result_list.pop()
    root.update()


def show_result_frame():
    listbox = tk.Listbox(root, listvariable=result_list_var)
    listbox.pack(expand=1, fill=tk.X)
    frame = tk.Frame(root)
    minus_button = tk.Button(root, text='-', command=del_result_value)
    minus_button.pack(side=tk.RIGHT)
    frame.pack(expand=1, fill=tk.X)


if __name__ == '__main__':
    show_result_frame()
    root.mainloop()
