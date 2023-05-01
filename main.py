import tkinter as tk


root = tk.Tk()

result_listbox = tk.Listbox(root)
listbox_vars = []


class AssistWindow(tk.Toplevel):
    """Вспомогательное окно для занесения информации"""
    def __init__(self, parent_root):
        super().__init__(master=parent_root)
        self.__main()

    def __main(self):
        self.config(border=1, relief='solid')
        self.show_entry_frames()
        self.grab_set()
        self.focus_set()
        self.wait_window()
        pass

    def show_entry_frames(self):
        lbl1 = tk.Label(self, text='Введите номер заказа')
        lbl1.pack(anchor=tk.NW)
        entry1 = tk.Entry(self)
        entry1.pack()


class WorkFrame:
    """Объект для хранения информации о парных виджетов и функции работы с ними"""
    def __init__(self, lbl, side):
        self.lbl = lbl
        self.side = side

    def show_work_frame(self):
        frame = tk.Frame(root)
        label = tk.Label(frame, text=self.lbl)
        label.pack(expand=1, fill=tk.X)
        list_box = tk.Listbox(frame, height=20)
        listbox_vars.append(list_box)
        list_box.pack(expand=1, fill=tk.BOTH)
        button_frame = tk.Frame(frame)
        button_frame.pack(expand=1, fill=tk.X)
        plus_button = tk.Button(button_frame, text='+', width=4, font='arial 12 bold', command=self.plus_func)
        plus_button.pack(side=tk.LEFT, expand=1, fill=tk.X)
        minus_button = tk.Button(button_frame, text='–', width=4, font='arial 12 bold', command=self.minus_func)
        minus_button.pack(side=tk.RIGHT, expand=1, fill=tk.X)
        frame.pack(side=self.side, expand=1, fill=tk.X)

    def plus_func(self):
        AssistWindow(root)
        
    def minus_func(self):
        lst_ind = 0
        if self.lbl == 'Развороты':
            lst_ind = 1
        elem_ind = listbox_vars[lst_ind].curselection()
        if elem_ind:
            listbox_vars[lst_ind].delete(*elem_ind)


def show_result_frame():
    result_listbox.pack(expand=1, fill=tk.BOTH)
    minus_button = tk.Button(root, text='–', width=4, font='arial 12 bold')
    minus_button.pack(anchor=tk.E)


if __name__ == '__main__':
    show_result_frame()
    left = WorkFrame('Обложки', tk.LEFT)
    right = WorkFrame('Развороты', tk.RIGHT)
    left.show_work_frame()
    right.show_work_frame()
    root.mainloop()
