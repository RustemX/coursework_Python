from tkinter import *
from tkinter import ttk     # подключаем пакет ttk

main_window = Tk()     # создаем корневой объект - окно
main_window.title("Приложение на Tkinter")     # устанавливаем заголовок окна
main_window.geometry("300x250")    # устанавливаем размеры окна
main_window.update_idletasks()
print(main_window.geometry())


label = Label(text=main_window.geometry()) # создаем текстовую метку
label.pack()    # размещаем метку в окне

main_window.mainloop()