import tkinter as tk
import tkinter.font as tkFont

class input_main(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.grid()
    self.creatDefine()
    self.creat_input()
    self.button_set()
  def creatDefine(self):
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    self.print = tk.Label(self, text = '請輸入固定事項:', font = font1)
    self.print.grid(row = 0,column = 0, columnspan = 4, sticky = tk.W)
  def creat_input(self):
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    self.inputbox_event = tk.Text(self, height = 1, width = 7,font = font1)
    self.ee = tk.Label(self, text = ' : ', font = font1)
    self.inputbox_time_1 = tk.Text(self, height = 1, width = 7,font = font1)
    self.cc = tk.Label(self, text = '---', font = font1)
    self.inputbox_time_2 = tk.Text(self, height = 1, width = 7,font = font1)
    
    self.inputbox_event.grid(row = 1, column = 0, sticky = tk.W)
    self.ee.grid(row = 1, column = 1, sticky = tk.W)
    self.inputbox_time_1.grid(row = 1, column = 2, sticky = tk.W)
    self.cc.grid(row = 1, column = 3, sticky = tk.W)
    self.inputbox_time_2.grid(row = 1, column = 4, sticky = tk.W)
  def button_set(self):
    font1 = tkFont.Font(size = 15, family = 'Times New Roman')
    self.next = tk.Button(self, text = '輸入下一個', font = font1)
    self.fin = tk.Button(self, text = '完成輸入，進入下一頁', font = font1)
    self.next.grid(row = 3, column = 0, columnspan = 4, sticky = tk.W)
    self.fin.grid(row = 5, column = 0, columnspan = 4, sticky = tk.W)
  #def button_function(self):
    
cal = input_main()
cal.master.title('行事曆產生器')
cal.mainloop()