import tkinter as tk

class Calender_main(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.grid()
    self.createDays()
    self.createTimes() 
  def createDays(self):
    column_weekdays = tk.Label(self, text = '一 二 三 四 五 六 日')
    column_weekdays.grid(row = 0,column = 1)
  def createTimes(self):
    row_times = tk.Label(self, text = '8.10')
    row_times.grid(row = 1,column = 0)  
cal = Calender_main()
cal.master.title('日歷')
cal.mainloop()