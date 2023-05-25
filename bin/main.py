import tkinter as tk
import tkinter.font as tkFont

class Calender_main(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.grid()
    self.createDays()
    self.createTimes() 
    self.creatWidget()
  def createDays(self):
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    column_weekdays = tk.Label(self, text = '一 二 三 四 五 六 日', height = 1,\
                               width = 16, font = font1)   
    column_weekdays.grid(row = 0, column = 1, columnspan = 7)
  def createTimes(self):
    font2 = tkFont.Font(size = 18, family = 'Times New Roman')
    row_times = tk.Label(self, text = '8.10', font = font2)
    row_times.grid(row = 1,column = 0)  
  def creatWidget(self):
    font3 = tkFont.Font(size = 18, family = 'Times New Roman')
    workAppend = tk.Button(self, text = '[]',height = 3, width = 9,font = font3)
    workAppend.grid(row = 1, column = 1)
cal = Calender_main()
cal.master.title('日歷')
cal.mainloop()