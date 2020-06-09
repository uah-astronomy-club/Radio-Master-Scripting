# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:33:48 2020

@author: Brandon Staton
"""
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from intvalidate import int_validate
root=Tk()
root.title('UAH Astronomy Club')
# root.geometry('500x500')

#------------------------------------------------------------------------------
# Object Info

# Object info frame
object_frame = LabelFrame(root, text = 'Object Information', padx = 5, pady=5)
object_frame.grid(row = 0, column = 0, padx=10, pady=10)


# Object coordinate buttons
object_input_method = IntVar()
object_input_method.set(1)
object_input_method_value = 1

# button click function
def btclicked(value):
    object_input_method_value = int(value)
    dropdown_enabler()
    azel_enabler()
    gal_enabler()
    print(object_input_method_value)

# Defining the buttons
Bt1 = Radiobutton(object_frame, text = 'Listed Object', variable = object_input_method, 
                  value = 1, command = lambda: btclicked(object_input_method.get()))
Bt2 = Radiobutton(object_frame, text = 'Azel Coordinates', variable = object_input_method, 
                  value = 2, command = lambda: btclicked(object_input_method.get()))
Bt3 = Radiobutton(object_frame, text = 'Gal Coordinates', variable = object_input_method, 
                  value = 3, command = lambda: btclicked(object_input_method.get()))

Bt1.grid(row = 0, column = 0, sticky = W)
Bt2.grid(row = 1, column = 0, sticky = W)
Bt3.grid(row = 2, column = 0, sticky = W)



# Known objects dropdown menu
def selected(event):
    selected_object = objectBox.get()
    print(selected_object)

f = open('SRTObjects.txt','r')
content = f.read().split()
f.close()

clicked = StringVar()
clicked.set(content[0])

def dropdown_enabler():
    if object_input_method.get() !=1:
        objectBox.config(state = DISABLED)
    else:
        objectBox.config(state = 'readonly') 
objectBox = ttk.Combobox(object_frame, value=content, state = 'readonly')
objectBox.current(0)
objectBox.bind('<<ComboboxSelected>>',selected)
objectBox.grid(row = 0, column = 1, padx=10, columnspan = 3)


# Azel coor input
def azel_enabler():
    if object_input_method.get() !=2:
        az_value.config(state = DISABLED)
        el_value.config(state=DISABLED)
    else:
        az_value.config(state = NORMAL)
        el_value.config(state=NORMAL)
        
az_text = Label(object_frame, text = 'Azimuth:')
az_text.grid(row = 1, column = 1)
az_value = Spinbox(object_frame, from_=0, to=359, width = 4)
int_validate(az_value, limits = (0,359))
az_value.grid(row = 1, column = 2)

el_text = Label(object_frame, text = 'Elevation:')
el_text.grid(row = 1, column = 3)
el_value = Spinbox(object_frame, from_=0, to=90, width = 3)
int_validate(az_value, limits = (0,90))
el_value.grid(row = 1, column = 4)

# Azel and elevation input fields start disabled
az_value.config(state = DISABLED)
el_value.config(state=DISABLED)

# Gal coor input
def gal_enabler():
    if object_input_method.get() !=3:
        lat_value.config(state = DISABLED)
        lon_value.config(state=DISABLED)
    else:
        lat_value.config(state = NORMAL)
        lon_value.config(state=NORMAL)
        
lat_text = Label(object_frame, text = 'Latitude:')
lat_text.grid(row = 2, column = 1)
lat_value = Spinbox(object_frame, from_=0, to=359, width = 4)
int_validate(lat_value, limits = (0,359))
lat_value.grid(row = 2, column = 2)

lon_text = Label(object_frame, text = 'Longitude:')
lon_text.grid(row = 2, column = 3)
lon_default = StringVar(root)
lon_default.set('0')
lon_value = Spinbox(object_frame, from_=-90, to=90, width = 3, textvariable = lon_default)
int_validate(lon_value, limits = (-90,90))
lon_value.grid(row = 2, column = 4)

# lat and lon input fields start disabled
lat_value.config(state = DISABLED)
lon_value.config(state=DISABLED)



# #------------------------------------------------------------------------------
# Current time and date
time_now = datetime.now()
current_year = int(time_now.year)
current_month=int(time_now.month)
current_day=int(time_now.day)
current_hr = int(time_now.hour)
current_min =int(time_now.minute)
current_sec = int(time_now.second)
today = datetime.today()

# Default time value
am_pm_default = 0
if current_hr == 0:
    current_hr = 12
    am_pm_default = 0
elif current_hr == 12:
    am_pm_default = 1
else:
    current_hr = current_hr - 12
    am_pm_default = 1

date_time_frame = LabelFrame(root, text = 'Date and Time of Observation', 
                             padx = 5, pady=5)
date_time_frame.grid(row = 1, column = 0, padx=10, pady=10)

# Date picker
cal = Calendar(date_time_frame, selectmode='day',year=current_year,month=current_month,
                day=current_day, mindate=today)
cal.grid(row = 0, column = 0, padx = 31, columnspan = 5)

# Time picker
time_text = Label(date_time_frame, text = 'Time of observation: ', pady = 10)
time_text.grid(row = 1, column = 0)

# hour picker
hr_default = StringVar(root)
hr_default.set(current_hr)
hr = Spinbox(date_time_frame, from_=1, to=12, width = 3, textvariable = hr_default)
hr.grid(row = 1, column = 1)

# minute picker
min_default = StringVar(root)
min_default.set(current_min)
minute = Spinbox(date_time_frame, from_ = 00, to=59, width = 3, format="%02.0f",
                 textvariable = min_default)
int_validate(minute, limits = (00,59))
minute.grid(row = 1, column = 2)

# second picker
sec_default = StringVar(root)
sec_default.set(current_sec)
second = Spinbox(date_time_frame, from_=00, to = 59, width = 3, format="%02.0f",
                 textvariable = sec_default)
int_validate(second, limits = (00,59))
second.grid(row = 1, column = 3)

def am_pm_selected(event):
    am_pm_value = am_pm.get()
    print(am_pm_value)


am_pm = ttk.Combobox(date_time_frame, value=['AM', 'PM'], state = 'readonly', width = 3)
am_pm.current(am_pm_default)
am_pm.bind('<<ComboboxSelected>>',am_pm_selected)
am_pm.grid(row = 1, column = 4, padx=10, columnspan = 3)

def time_validator(obs_date, hr, mn, sec, am_pm):
    inputted_date_int = [0,0,0]
    inputted_date = obs_date.split('/')
    global time_valid
    time_valid = True
    if am_pm == "PM":
        hr = hr + 12
    inputted_date[2] = '20'+inputted_date[2]
    inputted_date_int[0] = int(inputted_date[0])
    inputted_date_int[1] = int(inputted_date[1])
    inputted_date_int[2] = int(inputted_date[2])
    
    if inputted_date_int[2] == int(time_now.year):
        if inputted_date_int[0] == int(time_now.month):
            if inputted_date_int[1] == int(time_now.day):
                if hr < int(time_now.hour):
                    time_valid = False
                    print(time_valid)
                elif hr == int(time_now.hour):
                    if mn < int(time_now.minute):
                        time_valid = False
                        print(time_valid)
                    elif mn == int(time_now.minute):
                        if sec <= int(time_now.second):
                            time_valid = False
                            print(time_valid)
    return time_valid
    
    
    

#------------------------------------------------------------------------------
# Confirm and exit buttons
def error_time():
    messagebox.showwarning('Error','Inputted Time is not Valid.')

def confirm_click():
    obs_date = cal.get_date()
    obs_date = str(obs_date)
    obs_hr = int(hr.get())
    obs_min = int(minute.get())
    obs_sec = int(second.get())
    obs_am_pm = am_pm.get()
    validation = time_validator(obs_date, obs_hr, obs_min, obs_sec, obs_am_pm)
    if validation == False:
        error_time()
        
    
    print(obs_date)
    
confirm_button = Button(root, text = 'Confirm', command = confirm_click)
confirm_button.grid(row = 999, column = 998)


exit_button = Button(root, text = 'Exit', command = root.destroy)
exit_button.grid(row = 999, column = 999)

mainloop()

'''
Things to add:
    Clock with the current time at the top of this program
    Remove print statements
'''
