import tkinter as tk
from time import strftime
import datetime
from playsound import playsound

root = tk.Tk()
root.title("Kripa's Clock")

# Variables to store alarm time
alarmHour = None
alarmMin = None
alarmSet = False  # To check if an alarm is set

# Function to set the alarm
def set_alarm():
    global alarmHour, alarmMin, alarmSet
    alarmHour = int(alarm_hour_entry.get())
    alarmMin = int(alarm_min_entry.get())
    alarmSet = True
    alarm_status_label.config(text=f"Alarm set for {alarmHour:02}:{alarmMin:02}", fg="green")

# Function to update the clock and check the alarm
def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    
    # Check if it's time for the alarm
    now = datetime.datetime.now()
    if alarmSet and now.hour == alarmHour and now.minute == alarmMin:
        playsound("rooster.mp3")  
        alarm_status_label.config(text="Alarm ringing!", fg="red")
    
    label.after(1000, time)  # Update every second

#display
label = tk.Label(root, font=("calibri", 30, 'bold'), background='beige', foreground='crimson')
label.pack(anchor='center')

# Alarm input fields and button
tk.Label(root, text="Set Alarm (HH:MM)").pack()
alarm_hour_entry = tk.Entry(root, width=5)
alarm_hour_entry.pack(side='left')
alarm_min_entry = tk.Entry(root, width=5)
alarm_min_entry.pack(side='left')
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()

# Alarm status
alarm_status_label = tk.Label(root, text="", font=("calibri", 20), background='beige', foreground='blue')
alarm_status_label.pack()

time() 

root.mainloop()
