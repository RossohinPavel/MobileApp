import tkinter as tk


root = tk.Tk()

result_listbox = tk.Listbox(root)
listbox_vars = []


class AssistWindow(tk.Toplevel):
    """Вспомогательное окно для занесения информации"""
    def __init__(self, parent_root, cell):
        super().__init__(master=parent_root)
        self.cell = cell
        self.order_name = tk.StringVar()
        self.book_qty = tk.StringVar()
        self.pages_qty = tk.StringVar()
        self.__main()
        
    def __main(self):
        self.config(border=1, relief='solid')
        self.show_order_entry_frame()
        self.show_quantity_frame(0, 'Количество', self.book_qty, 'Добавить', self.add_func)
        self.show_quantity_frame(2, 'Развороты', self.pages_qty, 'Отмена', self.destroy)
        self.to_desctop_center()
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.wait_window()

    def to_desctop_center(self):
        self.update_idletasks()
        parent_width = root.winfo_width()
        parent_height = root.winfo_height()
        parent_place_x = root.winfo_x()  
        parent_place_y = root.winfo_y()
        child_width = self.winfo_width()
        child_height = self.winfo_height()
        place_x = ((parent_width - child_width) // 2) + parent_place_x + 10
        place_y = ((parent_height - child_height) // 2) + parent_place_y - 100
        self.geometry(f"+{place_x}+{place_y}")

    def show_order_entry_frame(self):
        lbl1 = tk.Label(self, text='Введите номер заказа')
        lbl1.grid(row=0, column=0, columnspan=3)
        entry1 = tk.Entry(self, font='Arial 20', width=14, textvariable=self.order_name)
        entry1.grid(row=1, column=0, columnspan=3)

    def show_quantity_frame(self, column, lbl_txt, entry_var, btn_txt, btn_fx):
        lbl = tk.Label(self, text=lbl_txt)
        lbl.grid(row=2, column=column)
        entry = tk.Entry(self, font='Arial 20', width=6, textvariable=entry_var)
        entry.grid(row=3, column=column)
        if column == 0:
            separator = tk.Label(self, text='/')
            separator.grid(row=3, column=1)
        add_btn = tk.Button(self, text=btn_txt, command=btn_fx, font='Arial 14')
        add_btn.grid(row=4, column=column)

    def add_func(self):
        lst_ind = 1 if self.cell == 'Развороты' else 0
        order_name, book_qty, page_qty = self.order_name.get(), self.book_qty.get(), self.pages_qty.get()
        if not order_name or not book_qty or not page_qty:
            return
        string = f'{order_name} - {book_qty}/{page_qty}'
        listbox_vars[lst_ind].insert(0, string)
        self.destroy()



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
        AssistWindow(root, self.lbl)
        
    def minus_func(self):
        lst_ind = 1 if self.lbl == 'Развороты' else 0
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
