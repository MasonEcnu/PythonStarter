#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.quit_button = Button(self, text="Quit", command=self.quit)
        self.hello_label = Label(self, text="Hello, world!")
        self.name_input = Entry(self)
        self.alert_button = Button(self, text="Hello", command=self.hello)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # pack()方法把Widget加入到父容器中，并实现布局
        self.quit_button.pack()
        self.hello_label.pack()
        self.name_input.pack()
        self.alert_button.pack()

    def hello(self):
        name = self.name_input.get() or "World!"
        messagebox.showinfo("Message", "Hello %s" % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
