import tkinter as tk
import tkinter.font as tkFont
import calendar
import datetime
from datetime import datetime, timedelta, date
from collections import defaultdict

import tkinter as tk
import tkinter.font as tkFont

class input_main(tk.Frame):
  def __init__(self,return_input):
    tk.Frame.__init__(self)
    self.configure(bg = 'azure')
    self.grid()
    self.creatDefine()
    self.creat_input()
    self.button_set()
    
  def creatDefine(self):
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    self.print = tk.Label(self, text = '請輸入固定事項:', font = font1)
    self.print.grid(row = 0,column = 0, columnspan = 4, sticky = tk.W)
    self.print.configure(bg = 'azure')
    
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
    self.reminder.configure(bg = 'azure')
    self.reminder = tk.Label(self, text = '時間輸入格式是HH:MM,24小時制', font = font1)
    self.reminder.grid(row = 4,column = 0, columnspan = 4, sticky = tk.W)
    self.reminder.configure(bg = 'azure')
    
    self.named.grid(row = 1, column = 0, columnspan = 2, sticky = tk.W)
    self.inputbox_event.grid(row = 1, column = 2, sticky = tk.W)
    self.named.configure(bg = 'azure')
    self.inputbox_event.configure(bg = 'lightcyan')
    
    self.dateName.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W)
    self.inputbox_Date.grid(row = 2, column = 2, sticky = tk.W)
    self.inputbox_time_1.grid(row = 2, column = 3, sticky = tk.W)
    self.cc.grid(row = 2, column = 4, sticky = tk.W)
    self.inputbox_time_2.grid(row = 2, column = 5, sticky = tk.W)
    self.dateName.configure(bg = 'azure')
    self.inputbox_Date.configure(bg = 'lightcyan')
    self.inputbox_time_1.configure(bg = 'lightcyan')
    self.cc.configure(bg = 'azure')
    self.inputbox_time_2.configure(bg = 'lightcyan')
    
  def button_set(self):
    font1 = tkFont.Font(size = 15, family = 'Times New Roman')
    self.next = tk.Button(self, text = '輸入下一個', font = font1,\
                          activebackground='turquoise',
                          command = lambda: self.button_function_collect(return_input))
    self.fin = tk.Button(self, text = '完成輸入，進入下一頁', font = font1,\
                         activebackground='turquoise',
                         command= lambda: self.button_function_return(return_input))
    self.next.grid(row = 5, column = 0, columnspan = 4, sticky = tk.W)
    self.fin.grid(row = 6, column = 0, columnspan = 4, sticky = tk.W)
    self.next.configure(bg = 'paleturquoise')
    self.fin.configure(bg = 'paleturquoise')
    
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
    self.configure(bg = 'azure')
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
    
    self.print.configure(bg = 'azure')
    self.def_1.configure(bg = 'azure')
    self.def_2.configure(bg = 'azure')
    self.def_3.configure(bg = 'azure')
    self.def_4.configure(bg = 'azure')
    
    self.reminder = tk.Label(self, text = '日期輸入格式為YYYY-MM-DD', font = font1)
    self.reminder.grid(row = 9,column = 0, columnspan = 4, sticky = tk.W)
    self.reminder.configure(bg = 'azure')
    
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
    
    self.inputbox_event.configure(bg = 'lightcyan')
    self.inputbox_importance.configure(bg = 'lightcyan')
    self.inputbox_time_long.configure(bg = 'lightcyan')
    self.inputbox_deadline.configure(bg = 'lightcyan')

  def button_set(self):
    font1 = tkFont.Font(size = 15, family = 'Times New Roman')
    self.next = tk.Button(self, text = '輸入下一個', font = font1,\
                          activebackground='turquoise',\
                          command = lambda: self.button_function_collect(return_input_2))
    self.fin = tk.Button(self, text = '完成輸入，進入下一頁', font = font1,\
                         activebackground='turquoise',\
                         command= lambda: self.button_function_return(return_input_2))
    self.next.grid(row = 10, column = 0, columnspan = 4, sticky = tk.W)
    self.fin.grid(row = 11, column = 0, columnspan = 4, sticky = tk.W)
    self.next.configure(bg = 'paleturquoise')
    self.fin.configure(bg = 'paleturquoise')
    
  def button_function_collect(self,return_input_2):
    if self.inputbox_event.get(0.0, 'end') != '' and\
       self.inputbox_importance.get(0.0, 'end') != '' and\
       self.inputbox_time_long.get(0.0, 'end') != '' and\
       self.inputbox_deadline.get(0.0, 'end') != '' :
      return_input_2.append([self.inputbox_event.get(0.0, 'end-1c')\
                           ,int(self.inputbox_importance.get(0.0, 'end-1c'))\
                           ,int(self.inputbox_time_long.get(0.0, 'end-1c'))\
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

# 固定List == 名稱, 日期, 開始, 結束
# 排程list == 名稱, 重要度, 大約需要時間,截止時間
#重要程度 1,2,3
#若時間衝突到，就先做1
#1 : 時間內一定要做完 優先順位最高 
#2 : 時間內一定要做完
#3 :時間內能做完最好 沒做完也沒差   
# 找差距最少的
#空閒時間完成
#找enoughtime
#排進schedule

cur_day = datetime.now().date()

class Calender_schedule:

    def __init__(self):
        self.events = defaultdict(dict)
    
    def add_fixed_event(self,name, date, start_time, end_time):  #綁定到固定輸入畫面的完成輸入 #重複的固定時間要排除
        
        event = {'start_time': start_time, 'end_time':end_time, 'name': name}
        self.events[date][start_time] = event

    def find_recent_day(self):
        sorted_events = sorted(self.events.items(), key=lambda x: (x[0], x[1]))
        recent_day = sorted_events[0][0]

        return recent_day

    def view_calendar(self):
        sorted_events = sorted(self.events.items(), key=lambda x: (x[0], x[1]))
        output_cal = []
        for date, events in sorted_events:
            #print(f"Date: {date}")
            sorted_events_by_time = sorted(events.items(), key=lambda x: x[0])
            for start_time, event in sorted_events_by_time:
                #print(f"  - {start_time} to {event['end_time']}: {event['name']}")
                output_cal.append([date[0:4], date[5:7], date[8:], start_time, event['end_time'], event['name']])
        return output_cal
        
    def find_spacetime(self, date):
        events = self.events.get(date, {})  #starttime, event
        sorted_events = sorted(events.items())
        free_time_slots = []
        totaltime = timedelta()
        prev_end_time = datetime.strptime('08:00', '%H:%M')
        end_of_day = datetime.strptime('21:00', '%H:%M') 


        if len(sorted_events) != 0: 

            for start_time, event in sorted_events:
                current_start_time = datetime.strptime(start_time, '%H:%M')
                current_end_time = datetime.strptime(event['end_time'], '%H:%M')
                totaltime += current_end_time - current_start_time
                if prev_end_time < current_start_time:  # 存在空閒時間段
                    time_left = current_start_time - prev_end_time
                    free_time_slots.append((prev_end_time, current_start_time, time_left))  

                prev_end_time = current_end_time
            
            # 檢查最後一個事件之後是否存在空閒時間段
            last_event = sorted_events[-1][1]
            last_event_end_time = datetime.strptime(last_event['end_time'], '%H:%M')
            if last_event_end_time < end_of_day:
                time_left = end_of_day - last_event_end_time
                free_time_slots.append((last_event_end_time, end_of_day, time_left))
        else:
            time_left = end_of_day - prev_end_time
            free_time_slots.append ((prev_end_time, end_of_day, time_left))

        return free_time_slots, totaltime


    def find_total_spacetime(self,l1st):  #找那幾天的空閒時間
        total_spacetime = defaultdict(dict)
        totaltime = defaultdict(dict)
        for date in l1st:
            date_str = date.strftime('%Y-%m-%d')  # 將日期轉換為字串格式
            spacetime, total_time_perday = self.find_spacetime(date_str)
            total_spacetime[date_str] = spacetime
            totaltime[date_str] = total_time_perday

        return total_spacetime, totaltime
        
    # def find_enough_time(self):   #迴圈找enough
    #     self.demandtime = self[]
        

def days_until_target_date(recent_day,target_date):

    recent_day = datetime.strptime(recent_day, '%Y-%m-%d')
    datetime_obj = datetime.strptime(target_date, '%Y-%m-%d %H:%M:%S')
    time_difference = datetime_obj - recent_day 

    return time_difference

def days_need_to_be_considered (recent_day,l1st):  #需要考慮的日期

    target_day = max(l1st, key=lambda schedule: days_until_target_date(recent_day,schedule[3]))
    datetime_obj = datetime.strptime(target_day[3], '%Y-%m-%d %H:%M:%S')
    recent_day = datetime.strptime(recent_day, '%Y-%m-%d').date()
    target_date = datetime_obj.date()
    consider_days = []
    while recent_day<= target_date:
        consider_days.append(recent_day)
        recent_day += timedelta(days=1)
    return consider_days

# 演算  找enoughtime 然後不超過10小時 不過23:59 若時間到之前超過10小時也沒辦法
def scheduledEvent(recent, l1st):
    sorted_list1 = sorted(filter(lambda schedule: schedule[1] <= 2, l1st), key=lambda schedule: (days_until_target_date(recent,schedule[3]), schedule[1], schedule[2]))
    sorted_list2 = sorted(filter(lambda schedule: schedule[1] > 2, l1st), key=lambda schedule: (days_until_target_date(recent, schedule[3]), schedule[1], schedule[2]))
    merged_list = sorted_list1 + sorted_list2

    return merged_list


def to_algorithm(fixedtimetable, demand):
    duration_hours = demand[2]
    duration = timedelta(hours=duration_hours)
    times = []

    for date in fixedtimetable:
        if datetime.strptime(date, '%Y-%m-%d') <= datetime.strptime(demand[3], '%Y-%m-%d %H:%M:%S'):
            for values in fixedtimetable[date]:
                if values[-1] >= duration:
                    closein = values[-1] - duration
                    times.append([closein, date, values[0]])
    if times != []:
        times_sorted = sorted(times)
        out_put = [demand[0], times_sorted[0][1], times_sorted[0][2].strftime('%H:%M'), (times_sorted[0][2] + duration).strftime('%H:%M')]  # # 固定List == 名稱, 日期, 開始, 結束
    else:
        out_put = [demand[0]]
        #print(demand[0])
    return out_put

# 使用範例
a = [   ['Meeting','2023-07-28', '10:00', '12:00'],['Lunch','2023-07-28', '14:00', '15:30'],
        ['Meeting','2023-07-29', '09:00', '11:00'],['Lunch','2023-07-29', '12:00', '13:30'],
        ['Lunch','2023-07-30', '14:00', '15:30'],['tutor','2023-07-30', '19:00', '21:30'],
        ['trip','2023-07-31', '11:00', '15:30'],['Lunch','2023-08-01', '15:00', '21:30'],
        ['Lunch','2023-08-02', '09:00', '15:30'],['school','2023-08-03', '09:00', '15:30']
     ]

schedule_name = []
for i in a:
  schedule_name.append(i[0])
#之後用來比對

schedule_list1 = [
    ['Task1', 3, 4, '2023-08-01 16:00:00'],
    ['Task2', 1, 2, '2023-08-02 16:00:00'],
    ['Task3', 2, 3, '2023-08-01 16:00:00'],
    ['Task4', 2, 4, '2023-08-01 16:00:00'],
    ['Task5', 2, 15, '2023-08-01 16:00:00'],
    ['Task6', 2, 3, '2023-08-01 16:00:00'],
    ['Task7', 2, 3, '2023-08-01 16:00:00'],
    ['Task8', 2, 3, '2023-08-01 16:00:00'],
    ['Task9', 2, 15, '2023-08-01 16:00:00'],
    ['Task10', 2, 15, '2023-08-01 16:00:00'],
]   #  名稱, 重要度, 大約需要時間,截止時間

'''
a = cal.return_input

schedule_name = []
for i in a:
  schedule_name.append(i[0])
#之後用來比對

schedule_list1 = cal2.return_input
 #  名稱, 重要度, 大約需要時間,截止時間
'''

calendar = Calender_schedule()
for event_data in a:
    calendar.add_fixed_event(*event_data)    #把固定加進去
g = calendar.find_recent_day()
# print(g)
view = scheduledEvent(g,schedule_list1)  ##需要排程的list整理
# print(view)

# # 空閒時間段檢查
# #1.計算總共需要計算的時間
consider_day = days_need_to_be_considered(g,schedule_list1)
#print(consider_day)
test = consider_day[-1] - consider_day[0]

# #   2. 總共空閒時間
total_space_day, total_time_perday = calendar.find_total_spacetime(consider_day) 
cannot_be_schedule = []

for row in view:
    schedule_row = to_algorithm(total_space_day, row)
    if len(schedule_row) != 1:
        calendar.add_fixed_event(*schedule_row)
        # calendar.view_calendar()
        total_space_day, total_time_perday = calendar.find_total_spacetime(consider_day)
        #測試
        # for date, values in total_space_day.items():
        #     print(f"空閒時間 ({date}):")
        #     for start_time, end_time, time_left in values:
        #         print(f"  - {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}, left_time: {str(time_left)}")
        #     print(f"總花費時間 ({total_time_perday[date]})")         
    else:
        cannot_be_schedule.append(schedule_row)

calendar = Calender_schedule()
for event_data in a:
    calendar.add_fixed_event(*event_data)    #把固定加進去
# view = scheduledEvent(schedule_list1)  ##需要排程的list整理
# print(view)

# # 空閒時間段檢查
# #1.計算總共需要計算的時間
consider_day = days_need_to_be_considered(g,schedule_list1)
#print(consider_day)
test = consider_day[-1] - consider_day[0]
#print(test)
# #   2. 總共空閒時間
total_space_day, total_time_perday = calendar.find_total_spacetime(consider_day) 
cannot_be_schedule = []

cannot_be_schedule = []
for row in schedule_list1:
    schedule_row = to_algorithm(total_space_day, row)
    if len(schedule_row) != 1:
        calendar.add_fixed_event(*schedule_row)
        # calendar.view_calendar()
        total_space_day, total_time_perday = calendar.find_total_spacetime(consider_day)
        #測試
        # for date, values in total_space_day.items():
        #     print(f"空閒時間 ({date}):")
        #     for start_time, end_time, time_left in values:
        #         print(f"  - {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}, left_time: {str(time_left)}")
        #     print(f"總花費時間 ({total_time_perday[date]})")         
    else:
        cannot_be_schedule.append(schedule_row[0])

# 輸出 排進去的日曆 跟全部的剩餘時間
output = calendar.view_calendar()
#output的每一項是[YYYY,MM,DD,開始時間,結束時間,名稱]
day_list = []
for i in range(len(output)):
    day_now = output[i][1] + ':' +output[i][2]
    date_turn = datetime.strptime(day_now,"%m:%d")
    day_list.append(date_turn)
day_list.sort()
days_needed = abs(day_list[-1] - day_list[0])    
days_needed = days_needed.days+1

'''
for date, values in total_space_day.items():
    print(f"空閒時間 ({date}):")
    for start_time, end_time, time_left in values:
        print(f"  - {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}, left_time: {str(time_left)}")
    print(f"總花費時間 ({total_time_perday[date]})") 
# tests = ['Task1', 3, 11, '2023-06-01 16:00:00']        
# test1  = to_algorithm(total_space_day, tests)
# print(test1)
'''

#進入生出日曆的階段


class Calender_main(tk.Frame):
  def __init__(self):
    tk.Frame.__init__(self)
    self.configure(bg = 'azure')
    self.grid()
    self.createDays()
    self.createTimes() 
    self.creatWidget()
    self.schedule_generate()
    self.creat_none()
    
  def createDays(self):
    start_day = day_list[0]
    day_list_use = []
    for i in range(days_needed):
      day_now = start_day + timedelta(days = i)
      day_str = str(day_now.month)+'/'+str(day_now.day)
      day_list_use.append(day_str)
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    for i in range(days_needed):
      column_weekdays = tk.Label(self, text = str(day_list_use[i]), height = 1,\
                                 width = 3, font = font1)   
      column_weekdays.grid(row = 0, column = i+1, sticky = tk.W)
      column_weekdays.configure(bg = 'azure')
      
  def createTimes(self):
    font2 = tkFont.Font(size = 18, family = 'Times New Roman')
    for i in range(13):
      row_times = tk.Label(self, text = str(8+i)+'-'+str(8+i+1), font = font2)
      row_times.grid(row = i+1, column = 0)
      row_times.configure(bg = 'azure')
      
  def creatWidget(self):
    font3 = tkFont.Font(size = 18, family = 'Times New Roman')
    for i in range(1, days_needed+1):
    #橫
      for a in range(1,14):
      #直
        workAppend = tk.Button(self, text = '  ',height = 1, width = 4,font = font3)
        workAppend.grid(row = a, column = i)
        workAppend.configure(bg = 'azure')
        
  def widgetCommand(self): 
    newWindow = tk.Toplevel(self)
    font1 = tkFont.Font(size = 18, family = 'Times New Roman')
    title_now = tk.Text(newWindow, height = 1, width = 15,font = font1)
    remind = tk.Label(newWindow, text = '請輸入該事項的詳細資訊', font = font1)
    title_now.grid(row = 0,column = 0)
    remind.grid(row = 1,column = 0)
    a = tk.Text(newWindow, height = 7, width = 15,font = font1)
    a.grid(row = 2,column = 0)
    
  def schedule_generate(self):
  #output的每一項是[YYYY,MM,DD,開始時間,結束時間,名稱]
    font4 = tkFont.Font(size = 12, family = 'Times New Roman')
    output_processed = []
    date_first = day_list[0]
    
    for i in range(len(output)):
      date_now = output[i][1] + '/' + output[i][2]
      date_now = datetime.strptime(date_now, "%m/%d")
      column_now = (date_now - date_first).days + 1
      #處理每一項的column
      start_time = int(output[i][3][:2])
      end_time = int(output[i][4][:2])
      output_processed.append([column_now,(start_time-8+1),(end_time-8),output[i][5]])
    for i in output_processed:
      new_work = tk.Button(self, text = i[3],height = ((i[2])- i[1])*3,\
                           width = 4,font = font4,\
                           activebackground='turquoise',\
                           command = self.widgetCommand) 
      new_work.grid(row = i[1], column = i[0],rowspan = (i[2])\
                - i[1]+1) 
      if schedule_name.count(i[3]) != 0:        
        new_work.configure(bg="aquamarine")  
      else:
        new_work.configure(bg="skyblue")  
        
  def creat_none(self):
    if cannot_be_schedule != []:
      font1 = tkFont.Font(size = 18, family = 'Times New Roman')
      cant_title = tk.Label(self, text = '無法排入的事項:', font = font1) 
      cant_title.grid(row = 0, column = days_needed + 2,columnspan = 3) 
      cant_title.configure(bg = 'azure')      
      for i in range(len(cannot_be_schedule)):
        cant_arrange = tk.Label(self, text = cannot_be_schedule[i], font = font1) 
        cant_arrange.grid(row = i+1, column = days_needed + 2,columnspan = 3) 
        cant_arrange.configure(bg = 'azure')
cal = Calender_main()
cal.master.title('日歷')
cal.mainloop()