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
    for i in range(1, 8):
      column_weekdays = tk.Label(self, text = str(i), height = 1,\
                                 width = 1, font = font1)   
      column_weekdays.grid(row = 0, column = i)
  def createTimes(self):
    font2 = tkFont.Font(size = 18, family = 'Times New Roman')
    row_times = tk.Label(self, text = '8.10', font = font2)
    row_times.grid(row = 1,column = 0)  
  def creatWidget(self):
    font3 = tkFont.Font(size = 18, family = 'Times New Roman')
    for i in range(1, 8):
      for a in range(1, 9):
        workAppend = tk.Button(self, text = '[]',height = 1, width = 4,font = font3)
        workAppend.grid(row = a, column = i)
  #def creatButton(self):
  #def widgetCommand(self):
    
cal = Calender_main()
cal.master.title('日歷')
cal.mainloop()