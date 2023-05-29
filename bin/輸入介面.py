import tkinter as tk
import tkinter.font as tkFont

class input_main(tk.Frame):
  def __init__(self,return_input):
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
    self.inputbox_event = tk.Text(self, height = 1, width = 12,font = font1)
    self.named = tk.Label(self, text = ' 事件名稱： ', font = font1)
    self.dateName = tk.Label(self, text = ' 日期： ', font = font1)
    self.inputbox_Date = tk.Text(self, height = 1, width = 7,font = font1)
    self.inputbox_time_1 = tk.Text(self, height = 1, width = 7,font = font1)
    self.cc = tk.Label(self, text = '---', font = font1)
    self.inputbox_time_2 = tk.Text(self, height = 1, width = 7,font = font1)
    
    self.named.grid(row = 1, column = 0, columnspan = 2, sticky = tk.W)
    self.inputbox_event.grid(row = 1, column = 2, sticky = tk.W)
    
    self.dateName.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W)
    self.inputbox_Date.grid(row = 2, column = 2, sticky = tk.W)
    self.inputbox_time_1.grid(row = 2, column = 3, sticky = tk.W)
    self.cc.grid(row = 2, column = 4, sticky = tk.W)
    self.inputbox_time_2.grid(row = 2, column = 5, sticky = tk.W)
  def button_set(self):
    font1 = tkFont.Font(size = 15, family = 'Times New Roman')
    self.next = tk.Button(self, text = '輸入下一個', font = font1,\
                          command = lambda: self.button_function_collect(return_input))
    self.fin = tk.Button(self, text = '完成輸入，進入下一頁', font = font1,\
                         command= lambda: self.button_function_return(return_input))
    self.next.grid(row = 3, column = 0, columnspan = 4, sticky = tk.W)
    self.fin.grid(row = 5, column = 0, columnspan = 4, sticky = tk.W)
  def button_function_collect(self,return_input):
    if self.inputbox_event.get(0.0, 'end') != '' and\
       self.inputbox_Date.get(0.0, 'end') != '' and\
       self.inputbox_time_1.get(0.0, 'end') != '' and\
       self.inputbox_time_2.get(0.0, 'end') != '':
      return_input.append([self.inputbox_event.get(0.0, 'end-1c')\
                           ,self.inputbox_Date.get(0.0, 'end-1c')\
                           ,self.inputbox_time_1.get(0.0, 'end-1c')\
                           ,self.inputbox_time_2.get(0.0, 'end-1c')])
      self.inputbox_event.delete(0.0, 'end')
      self.inputbox_Date.delete(0.0, 'end')
      self.inputbox_time_1.delete(0.0, 'end')
      self.inputbox_time_2.delete(0.0, 'end')
    return return_input
  def button_function_return(self,return_input):
    self.return_input = return_input
    self.master.destroy()
return_input = []
import tkinter as tk
import tkinter.font as tkFont

class input_main(tk.Frame):
  def __init__(self,return_input):
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
    self.inputbox_event = tk.Text(self, height = 1, width = 12,font = font1)
    self.named = tk.Label(self, text = ' 事件名稱： ', font = font1)
    self.dateName = tk.Label(self, text = ' 日期： ', font = font1)
    self.inputbox_Date = tk.Text(self, height = 1, width = 12,font = font1)
    self.inputbox_time_1 = tk.Text(self, height = 1, width = 7,font = font1)
    self.cc = tk.Label(self, text = '---', font = font1)
    self.inputbox_time_2 = tk.Text(self, height = 1, width = 7,font = font1)
    
    self.reminder = tk.Label(self, text = '日期輸入格式為YYYY-MM-DD', font = font1)
    self.reminder.grid(row = 3,column = 0, columnspan = 4, sticky = tk.W)
    self.reminder = tk.Label(self, text = '時間輸入格式是HH:MM,24小時制', font = font1)
    self.reminder.grid(row = 4,column = 0, columnspan = 4, sticky = tk.W)
    
    
    self.named.grid(row = 1, column = 0, columnspan = 2, sticky = tk.W)
    self.inputbox_event.grid(row = 1, column = 2, sticky = tk.W)
    
    self.dateName.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W)
    self.inputbox_Date.grid(row = 2, column = 2, sticky = tk.W)
    self.inputbox_time_1.grid(row = 2, column = 3, sticky = tk.W)
    self.cc.grid(row = 2, column = 4, sticky = tk.W)
    self.inputbox_time_2.grid(row = 2, column = 5, sticky = tk.W)
  def button_set(self):
    font1 = tkFont.Font(size = 15, family = 'Times New Roman')
    self.next = tk.Button(self, text = '輸入下一個', font = font1,\
                          command = lambda: self.button_function_collect(return_input))
    self.fin = tk.Button(self, text = '完成輸入，進入下一頁', font = font1,\
                         command= lambda: self.button_function_return(return_input))
    self.next.grid(row = 5, column = 0, columnspan = 4, sticky = tk.W)
    self.fin.grid(row = 6, column = 0, columnspan = 4, sticky = tk.W)
  def button_function_collect(self,return_input):
    if self.inputbox_event.get(0.0, 'end') != '' and\
       self.inputbox_Date.get(0.0, 'end') != '' and\
       self.inputbox_time_1.get(0.0, 'end') != '' and\
       self.inputbox_time_2.get(0.0, 'end') != '':
      return_input.append([self.inputbox_event.get(0.0, 'end-1c')\
                           ,self.inputbox_Date.get(0.0, 'end-1c')\
                           ,self.inputbox_time_1.get(0.0, 'end-1c')\
                           ,self.inputbox_time_2.get(0.0, 'end-1c')])
      self.inputbox_event.delete(0.0, 'end')
      self.inputbox_Date.delete(0.0, 'end')
      self.inputbox_time_1.delete(0.0, 'end')
      self.inputbox_time_2.delete(0.0, 'end')
    return return_input
  def button_function_return(self,return_input):
    self.return_input = return_input
    self.master.destroy()
return_input = []
cal = input_main(return_input)
cal.master.title('輸入你的固定事項')
cal.mainloop()

#下面開始是第二個視窗

class input_todo(tk.Frame):
  def __init__(self,return_input):
    tk.Frame.__init__(self)
    self.grid()
    self.creatDefine()
    self.creat_input()
    self.button_set()
    
  def creatDefine(self):
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    self.print = tk.Label(self, text = '請輸入你的待辦事項:', font = font1)
    self.def_1 = tk.Label(self, text = '請輸入事件名稱:', font = font1)
    self.def_2 = tk.Label(self, text = '請輸入重要度:', font = font1)
    self.def_3 = tk.Label(self, text = '請輸入所需時間長度:', font = font1)
    self.def_4 = tk.Label(self, text = '請輸入截止日期:', font = font1)
  
    
    self.print.grid(row = 0,column = 0, columnspan = 4, sticky = tk.W)
    self.def_1.grid(row = 1,column = 0, columnspan = 4, sticky = tk.W)
    self.def_2.grid(row = 3,column = 0, columnspan = 4, sticky = tk.W)
    self.def_3.grid(row = 5,column = 0, columnspan = 4, sticky = tk.W)
    self.def_4.grid(row = 7,column = 0, columnspan = 4, sticky = tk.W)
    
    self.reminder = tk.Label(self, text = '日期輸入格式為YYYY-MM-DD', font = font1)
    self.reminder.grid(row = 9,column = 0, columnspan = 4, sticky = tk.W)
    
  def creat_input(self):
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    
    self.inputbox_event = tk.Text(self, height = 1, width = 15,font = font1)
    self.inputbox_importance = tk.Text(self, height = 1, width = 15,font = font1)
    self.inputbox_time_long = tk.Text(self, height = 1, width = 15,font = font1)
    self.inputbox_deadline = tk.Text(self, height = 1, width = 15,font = font1)
    #上面是所有需要考量的變數
    
    self.inputbox_event.grid(row = 2, column = 1, sticky = tk.W)
    self.inputbox_importance.grid(row = 4, column = 1, sticky = tk.W)
    self.inputbox_time_long.grid(row = 6, column = 1, sticky = tk.W)
    self.inputbox_deadline.grid(row = 8, column = 1, sticky = tk.W)

  def button_set(self):
    font1 = tkFont.Font(size = 15, family = 'Times New Roman')
    self.next = tk.Button(self, text = '輸入下一個', font = font1,\
                          command = lambda: self.button_function_collect(return_input_2))
    self.fin = tk.Button(self, text = '完成輸入，進入下一頁', font = font1,\
                         command= lambda: self.button_function_return(return_input_2))
    self.next.grid(row = 10, column = 0, columnspan = 4, sticky = tk.W)
    self.fin.grid(row = 11, column = 0, columnspan = 4, sticky = tk.W)
  def button_function_collect(self,return_input_2):
    if self.inputbox_event.get(0.0, 'end') != '' and\
       self.inputbox_importance.get(0.0, 'end') != '' and\
       self.inputbox_time_long.get(0.0, 'end') != '' and\
       self.inputbox_deadline.get(0.0, 'end') != '' :
      return_input_2.append([self.inputbox_event.get(0.0, 'end-1c')\
                           ,self.inputbox_importance.get(0.0, 'end-1c')\
                           ,self.inputbox_time_long.get(0.0, 'end-1c')\
                           ,self.inputbox_deadline.get(0.0, 'end-1c')+' '+'23:59:59'])
      self.inputbox_event.delete(0.0, 'end')
      self.inputbox_importance.delete(0.0, 'end')
      self.inputbox_time_long.delete(0.0, 'end')
      self.inputbox_deadline.delete(0.0, 'end')
    return return_input_2
  def button_function_return(self,return_input_2):
    self.return_input = return_input_2
    self.master.destroy()

return_input_2 = []
cal2 = input_todo(return_input_2)
cal2.master.title('輸入你的待辦事項')
cal2.mainloop()
print(cal.return_input,cal2.return_input)