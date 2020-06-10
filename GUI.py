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
import tkinter.scrolledtext as tkst
import sys
import time
import os
root=Tk()
root.title('UAH Astronomy Club')
root.iconbitmap('icon.ico')

#-----------------------------------------------------------------------------
# Clock Function

Clock_frame = LabelFrame(root, text = 'Current Time', padx = 130, pady = 5)
Clock_frame.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 2)

def clock():
    clock_hour = time.strftime('%I')
    clock_minute = time.strftime('%M')
    clock_second = time.strftime('%S')
    clock_am_pm = time.strftime('%p')
    time_zone = time.strftime('%Z')
    my_label.config(text = clock_hour + ':' + clock_minute + ':' + 
                    clock_second + ' ' + clock_am_pm)
    
    my_label2.config(text = time_zone)

    my_label.after(50, clock)


my_label = Label(Clock_frame, text = '', font =('Helvetica, 48'))
my_label2 = Label(Clock_frame, text = '')

my_label.pack(pady = 20)
my_label2.pack(pady = 20)

clock()


#------------------------------------------------------------------------------
# Object Info

# Object info frame
object_frame = LabelFrame(root, text = 'Object Information', padx = 5, pady=5)
object_frame.grid(row = 1, column = 0, padx=10, pady=10)


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
content.sort()
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
elif current_hr > 12:
    current_hr = current_hr - 12
    am_pm_default = 1
else:
    am_pm_default = 0

date_time_frame = LabelFrame(root, text = 'Date and Time of Observation', 
                             padx = 5, pady=5)
date_time_frame.grid(row = 2, column = 0, padx=10, pady=10)

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

# Gets if user selected AM or PM
def am_pm_selected(event):
    am_pm_value = am_pm.get()

# AM PM dropdown menu
am_pm = ttk.Combobox(date_time_frame, value=['AM', 'PM'], state = 'readonly', width = 3)
am_pm.current(am_pm_default)
am_pm.bind('<<ComboboxSelected>>',am_pm_selected)
am_pm.grid(row = 1, column = 4, padx=10, columnspan = 3)

# Validates if the inputted time has passed or not
def time_validator(obs_date, hr, mn, sec, am_pm):
    time_now = datetime.now()
    inputted_date_int = [0,0,0]
    inputted_date = obs_date.split('/')
    global time_valid
    time_valid = True
    if am_pm == "PM":
        hr = hr + 12
    if am_pm == 'AM' and hr == 12:
        hr = 0
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
# Integration Settings
Integration_frame = LabelFrame(root, text = 'Integration Settings', 
                             padx = 5, pady=5)
Integration_frame.grid(row = 1, column = 1, padx=10, pady=10)

# Inputted frequency validater
def freq_validate(event):
    if int(frequency_box.get()) < 1301 or int(frequency_box.get()) > 1799:
        freq_valid = False
        frequency_box.grid_forget() 
        freq_box_create()
    else:
        freq_valid = True

# Creation of box to input frequency
def freq_box_create():
    global frequency_box    
    frequency_box = Spinbox(Integration_frame, from_= 1301, to = 1799, width = 5)
    frequency_box.bind('<FocusOut>', freq_validate)
    frequency_box.grid(column = 1, row = 0)   

# initilizing center frequency input field
freq_box_create()
frequency_label = Label(Integration_frame, text = 'Center Frequency: ')
frequency_label.grid(column = 0, row = 0)
frequency_unit = Label(Integration_frame, text = 'MHz')
frequency_unit.grid(column = 2, row = 0)

# Observation Mode
obs_mode_text = Label(Integration_frame, text = 'Observation Mode: ')
obs_mode_text.grid(column =0 , row = 1)


def obs_selected(event):
    selected_obs_mode = obs_mode_value.get()
    print(selected_obs_mode)
    
obs_mode_click = StringVar()
obs_mode_click.set(0)
obs_mode_value = ttk.Combobox(Integration_frame, value = [1, 2, 3, 4], 
                              state = 'readonly', width = 3)
obs_mode_value.current(0)
obs_mode_value.bind('<<ComboboxSelected>>',obs_selected)
obs_mode_value.grid(column = 1, row = 1)

# Integration time
integration_time_text = Label(Integration_frame, text = 'Integration Time: ')
integration_time_text.grid(row = 2, column = 0)
integration_time_box = Spinbox(Integration_frame, from_= 1, to = 99999, width = 5)
int_validate(integration_time_box, limits = (1,99999))
integration_time_box.grid(column = 1, row = 2)
integration_time_units = Label(Integration_frame, text = ' Second(s)')
integration_time_units.grid(column = 2, row = 2)



# Calibration Time [seconds]
calibration_time_text = Label(Integration_frame, 
                              text = 'Time Between Calibrations: ')
calibration_time_text.grid(row = 3, column = 0)
calibration_time_box = Spinbox(Integration_frame, from_= 1, to = 99999, width = 5)
int_validate(calibration_time_box, limits = (1,99999))
calibration_time_box.grid(column = 1, row = 3)
calibration_time_units = Label(Integration_frame, text = ' Second(s)')
calibration_time_units.grid(column = 2, row = 3)


#------------------------------------------------------------------------------
# File Info
File_info_frame = LabelFrame(root, text = 'File Information', padx = 5,
                             pady = 5)
File_info_frame.grid(row = 2, column = 1, padx = 10, pady = 10)
temporary = Label(File_info_frame)
temporary.pack()

# Default file path
# .cmd file name
# .rad file name

#------------------------------------------------------------------------------
# Notification Box

Notification_frame = LabelFrame(root, text = 'Notifications', padx = 5,
                                pady = 5)
Notification_frame.grid(row = 0, column = 3, padx = 10, pady = 10, rowspan = 3,
                        columnspan = 3)

Notifications = tkst.ScrolledText(Notification_frame, width = 35, height = 37)
Notifications.pack()
# Notifications = Entry(Notification_frame)
Notifications.insert(INSERT,'Developed by Brandon Staton')
Notifications.insert(INSERT,'\nfor the UAH Astronomy Club')
Notifications.insert(INSERT, '\n\nThis program is a work in progress')
Notifications.insert(INSERT, '\n-----------------------------------\n')
Notifications.config(state = 'disabled')
# Notifications.pack(ipadx = 50, ipady = 300)

# Added [object] to [cmd file name]
# Added observation to [cmd file name]

#------------------------------------------------------------------------------
# Confirm and exit buttons

# popup error window if inputted time is not valid
def error_time():
    messagebox.showwarning('Error','Inputted Time is not Valid.')

# What to do when the confirm button is clicked
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
        Notifications.config(state = 'normal')
        Notifications.insert(INSERT, '\nError')
        Notifications.config(state = 'disabled')
    # Send notifcation to notification box

def Finalize():
    return

# Confirm Object button
confirm_button = Button(root, text = 'Confirm Object', command = confirm_click)
confirm_button.grid(row = 999, column = 3, padx = 5, pady = 5)

# All objects inputted
Finalize_button = Button(root, text = 'Finalize', command = Finalize)
Finalize_button.grid(row = 999, column = 4, padx = 5, pady = 5)


# Exit button
exit_button = Button(root, text = 'Exit', command = root.destroy)
exit_button.grid(row = 999, column = 5, padx = 5, pady = 5)

mainloop()