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
    row_times = tk.Label(self, text = '8', font = font2)
    row_times.grid(row = 1,column = 0) 
    row_times = tk.Label(self, text = '9', font = font2)
    row_times.grid(row = 2,column = 0)
    row_times = tk.Label(self, text = '10', font = font2)
    row_times.grid(row = 3,column = 0)
    row_times = tk.Label(self, text = '11', font = font2)
    row_times.grid(row = 4,column = 0)
    row_times = tk.Label(self, text = '12', font = font2)
    row_times.grid(row = 5,column = 0)
    row_times = tk.Label(self, text = '1', font = font2)
    row_times.grid(row = 6,column = 0)
    row_times = tk.Label(self, text = '2', font = font2)
    row_times.grid(row = 7,column = 0)
    row_times = tk.Label(self, text = '3', font = font2)
    row_times.grid(row = 8,column = 0)
    row_times = tk.Label(self, text = '4', font = font2)
    row_times.grid(row = 9,column = 0)
    row_times = tk.Label(self, text = '5', font = font2)
    row_times.grid(row = 10,column = 0)    
  def creatWidget(self):
    font3 = tkFont.Font(size = 18, family = 'Times New Roman')
    for i in range(1, 8):
      for a in range(1,11):
        workAppend = tk.Button(self, text = '[]',height = 1, width = 4,font = font3)
        workAppend.grid(row = a, column = i)

  #def widgetCommand(self): 還沒用到，預計是用來處理點擊每一個按鈕之後的command
    
cal = Calender_main()
cal.master.title('日歷')
cal.mainloop()