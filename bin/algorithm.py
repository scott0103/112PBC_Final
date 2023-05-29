import calendar
import datetime
from datetime import datetime, timedelta, date
from collections import defaultdict

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

    def view_calendar(self):
        sorted_events = sorted(self.events.items(), key=lambda x: (x[0], x[1]))
        for date, events in sorted_events:
            print(f"Date: {date}")
            sorted_events_by_time = sorted(events.items(), key=lambda x: x[0])
            for start_time, event in sorted_events_by_time:
                print(f"  - {start_time} to {event['end_time']}: {event['name']}")


    def find_spacetime(self, date):
        
        events = self.events.get(date, {})  #starttime, event
        sorted_events = sorted(events.items())
        free_time_slots = []
        totaltime = timedelta()
        prev_end_time = datetime.strptime('08:00', '%H:%M')
        end_of_day = datetime.strptime('00:00', '%H:%M') + timedelta(days=1)


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
        

def days_until_target_date(target_date):

    now = datetime.now()
    datetime_obj = datetime.strptime(target_date, '%Y-%m-%d %H:%M:%S')
    time_difference = datetime_obj - now

    return time_difference

def days_need_to_be_considered (l1st):  #需要考慮的日期

    target_day = max(l1st, key=lambda schedule: days_until_target_date(schedule[3]))
    today = datetime.now().date()
    datetime_obj = datetime.strptime(target_day[3], '%Y-%m-%d %H:%M:%S')
    target_date = datetime_obj.date()
    consider_days = []
    while today<= target_date:
        consider_days.append(today)
        today += timedelta(days=1)
    return consider_days

# 演算  找enoughtime 然後不超過10小時 不過23:59 若時間到之前超過10小時也沒辦法
def scheduledEvent(l1st):
    sorted_list1 = sorted(filter(lambda schedule: schedule[1] <= 2, l1st), key=lambda schedule: (days_until_target_date(schedule[3]), schedule[1], schedule[2]))
    sorted_list2 = sorted(filter(lambda schedule: schedule[1] > 2, l1st), key=lambda schedule: (days_until_target_date(schedule[3]), schedule[1], schedule[2]))
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
        out_put = demand[0]
    return out_put

# 使用範例
a = [   ['Meeting','2023-05-28', '10:00', '12:00'],['Lunch','2023-05-28', '14:00', '15:30'],
        ['Meeting','2023-05-29', '09:00', '11:00'],['Lunch','2023-05-29', '12:00', '13:30'],
        ['Lunch','2023-05-30', '14:00', '15:30'],['tutor','2023-05-30', '19:00', '21:30'],
        ['trip','2023-05-31', '11:00', '15:30'],['Lunch','2023-06-01', '15:00', '21:30'],
        ['Lunch','2023-06-02', '09:00', '15:30'],['school','2023-06-03', '09:00', '15:30']
     ]

schedule_list1 = [
    ['Task1', 3, 4, '2023-06-01 16:00:00'],
    ['Task2', 1, 2, '2023-06-02 16:00:00'],
    ['Task3', 2, 3, '2023-06-01 16:00:00'],
    ['Task4', 2, 4, '2023-06-01 16:00:00']
]   #  名稱, 重要度, 大約需要時間,截止時間

calendar = Calender_schedule()
for event_data in a:
    calendar.add_fixed_event(*event_data)    #把固定加進去
# view = scheduledEvent(schedule_list1)  ##需要排程的list整理
# print(view)

# 空閒時間段檢查
#1.計算總共需要計算的時間
consider_day = days_need_to_be_considered(schedule_list1)
#   2. 總共空閒時間
total_space_day, total_time_perday = calendar.find_total_spacetime(consider_day) 

for row in schedule_list1:
    cannot_be_schedule = []
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


# 輸出 排進去的日曆 跟全部的剩餘時間
calendar.view_calendar()
for date, values in total_space_day.items():
    print(f"空閒時間 ({date}):")
    for start_time, end_time, time_left in values:
        print(f"  - {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}, left_time: {str(time_left)}")
    print(f"總花費時間 ({total_time_perday[date]})") 
# tests = ['Task1', 3, 11, '2023-06-01 16:00:00']        
# test1  = to_algorithm(total_space_day, tests)
# print(test1)
    
