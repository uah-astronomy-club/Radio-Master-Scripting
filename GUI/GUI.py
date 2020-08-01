# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:33:48 2020

@author: Brandon Staton

This program takes user inputs and outputs a list of items to be observed along with
each items observation settings. The output list is sorted in ascending time order
of the user-inputted observations. The output list is formatted as follows:
    
    ['(directory to store files) (command file name) (rad file name)',
     '(object 1 info)', '(object 2 info)', ...]
    
Each of the objects info is formatted as follows:
    *For a listed object:
        'year-mo-dy hr:mn:sc Listed name center_freq observation_mode integration_time calibration_yes/no(1/2)'
        ex: '2020-06-11 20:00:00 Listed 50G 1301 1 1 1'
        
    *For an object with azel coordinates:
        'year-mo-dy hr:mn:sc Azel Az:el center_freq observation_mode integration_time calibration_yes/no(1/2)'
        ex: '2020-06-19 02:12:02 Azel 001:01 1301 1 1 1'
        Note: az is always a 3 digit number and lon is always a 2 digit number
        
    *For an object with galatic coordinates:
        'year-mo-dy hr:mn:sc Gal lat:lon center_freq observation_mode integration_time calibration_yes/no(1/2)'
        ex: '2020-06-19 02:15:02 Gal -01:001 1301 1 1 2'
        Note: lat is always a 3 digit number and lon is always a 2 digit number
    
    Note: Months, Days, Hours, Minutes, and Seconds are always 2 digit numbers
    
"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import *
from datetime import datetime
from intvalidate import int_validate
import tkinter.scrolledtext as tkst
import time
import os
import os.path
import webbrowser as wb
import GUI_Master_Writer as MW
import RAD_File_Checker as RFC

root=Tk()
root.title('UAH Astronomy Club')
root.iconbitmap('icon.ico')

#-----------------------------------------------------------------------------
# Clock Function

Clock_frame = LabelFrame(root, text = 'Current Time', padx = 190, pady = 5)
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

Bt1.grid(row = 0, column = 0, pady = 4, sticky = W)
Bt2.grid(row = 1, column = 0, pady = 4, sticky = W)
Bt3.grid(row = 2, column = 0, pady = 4 ,sticky = W)



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
el_value = Spinbox(object_frame, from_=0, to=90, width = 4)
int_validate(el_value, limits = (0,90))
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
lat_default = StringVar(root)
lat_default.set('0')
lat_value = Spinbox(object_frame, from_=-90, to=90, width = 4, textvariable = lat_default)
int_validate(lat_value, limits = (-90,90))
lat_value.grid(row = 2, column = 2)

lon_text = Label(object_frame, text = 'Longitude:')
lon_text.grid(row = 2, column = 3)
lon_default = StringVar(root)
lon_default.set('0')
lon_value = Spinbox(object_frame, from_=0, to=359, width = 4, textvariable = lon_default)
int_validate(lon_value, limits = (0,359))
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

date_time_frame = LabelFrame(root, text = 'Date and Time of Observation', 
                             padx = 5, pady=5)
date_time_frame.grid(row = 2, column = 0, padx=10, pady=10, rowspan = 4)

# Date picker
cal = Calendar(date_time_frame, selectmode='day',year=current_year,month=current_month,
                day=current_day, mindate=today)
cal.grid(row = 0, column = 0, padx = 31, columnspan = 5)

# Time picker
time_text = Label(date_time_frame, text = 'Time of observation: ', pady = 10)
time_text.grid(row = 1, column = 0)

# hour picker
global hr
hr_default = StringVar(root)
hr_default.set(12)
hr = Spinbox(date_time_frame,from_=1, to=12, width = 3, 
             textvariable = hr_default, wrap=True)
hr.grid(row = 1, column = 1)

# minute picker
global minute
min_default = StringVar(root)
min_default.set(00)
minute = Spinbox(date_time_frame, from_ = 00, to=59, width = 3, format="%02.0f",
                 textvariable = min_default, wrap=True)
int_validate(minute, limits = (00,59))
minute.grid(row = 1, column = 2)

# second picker
global second
sec_default = StringVar(root)
sec_default.set(00)
second = Spinbox(date_time_frame, from_=00, to = 59, width = 3, format="%02.0f",
                 textvariable = sec_default, wrap=True)
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
    if am_pm == "PM" and hr != 12:
        hr = hr + 12
    if am_pm == 'AM' and hr == 12:
        hr = 0
    inputted_date[2] = '20'+inputted_date[2]
    inputted_date_int[0] = int(inputted_date[0])
    inputted_date_int[1] = int(inputted_date[1])
    inputted_date_int[2] = int(inputted_date[2])
    
    if inputted_date_int[2] < int(time_now.year):
        time_valid = False
    elif inputted_date_int[2] == int(time_now.year):
        if inputted_date_int[0] < int(time_now.month):
            time_valid = False
        elif inputted_date_int[0] == int(time_now.month):
            if inputted_date_int[1] < int(time_now.day):
                time_valid = False
            elif inputted_date_int[1] == int(time_now.day):
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
                        else:
                            time_valid = True
                    else:
                        time_valid = True
                else:
                    time_valid = True
            else:
                time_valid = True
        else:
            time_valid = True
    else:
        time_valid  = True
    return time_valid

#------------------------------------------------------------------------------
# Integration Settings
Integration_frame = LabelFrame(root, text = 'Integration Settings', 
                             padx = 70, pady=5)
Integration_frame.grid(row = 1, column = 1, padx=10, pady=10)

# Inputted frequency validater
def freq_validate(event):
    freq_valid = True
    if str(frequency_box.get()).isdecimal() == True:
        if int(frequency_box.get()) < 1301 or int(frequency_box.get()) > 1799:
            freq_valid = False
            frequency_box.grid_forget() 
            freq_box_create()
    else:
        freq_valid = False

# Creation of box to input frequency
def freq_box_create():
    global frequency_box    
    frequency_box = Spinbox(Integration_frame, from_= 1301, to = 1799, width = 5)
    frequency_box.bind('<FocusOut>', freq_validate)
    frequency_box.grid(column = 1, row = 0, pady = 3)   

# initilizing center frequency input field
freq_box_create()
frequency_label = Label(Integration_frame, text = 'Center Frequency: ')
frequency_label.grid(column = 0, row = 0)
frequency_unit = Label(Integration_frame, text = 'MHz')
frequency_unit.grid(column = 2, row = 0)

# Observation Mode
obs_mode_text = Label(Integration_frame, text = 'Observation Mode: ')
obs_mode_text.grid(column =0 , row = 1, pady = 3)


def obs_selected(event):
    selected_obs_mode = obs_mode_value.get()
    print(selected_obs_mode)
    
obs_mode_click = StringVar()
obs_mode_click.set(0)
obs_mode_value = ttk.Combobox(Integration_frame, value = [1, 2, 3, 4], 
                              state = 'readonly', width = 3)
obs_mode_value.current(0)
obs_mode_value.bind('<<ComboboxSelected>>',obs_selected)
obs_mode_value.grid(column = 1, row = 1, pady = 3)

# Integration time
integration_time_text = Label(Integration_frame, text = 'Integration Time: ')
integration_time_text.grid(row = 2, column = 0)
integration_time_box = Spinbox(Integration_frame, from_= 1, to = 99999, width = 5)
int_validate(integration_time_box, limits = (1,99999))
integration_time_box.grid(column = 1, row = 2, pady = 3)
integration_time_units = Label(Integration_frame, text = ' Second(s)')
integration_time_units.grid(column = 2, row = 2)


# Calibration
calibrate = IntVar()
calibrate.set(1)

calibration_text = Label(Integration_frame, text = 'Auto Calibration: ')
calibration_text.grid(row = 3, column = 0)
calibrate_yes = Radiobutton(Integration_frame,text = 'Yes', variable = calibrate, value = 1)
calibrate_yes.grid(row = 3, column = 1)
calibrate_no = Radiobutton(Integration_frame,text='No', variable = calibrate, value = 2)
calibrate_no.grid(row = 3, column = 2)


#------------------------------------------------------------------------------
# File Info
File_info_frame = LabelFrame(root, text = 'File Information', padx = 8,
                             pady = 5)
File_info_frame.grid(row = 2, column = 1, padx = 10, pady = 10)

# ask user if they want to make selected directory the default directory
def def_file_path_popup():
    response = messagebox.askyesno('File Path', 'Make default file path?')
    if response == 1:
        global filename
        GD = open('GUI_Defaults.txt', 'w')
        GD.write(filename)
        GD.close()

# error handling for file path
def browse_directory():
    global filename
    filename = filedialog.askdirectory()
    if str(filename) != '':
        file_directory.config(state = NORMAL)
        file_directory.delete(0,END)
        file_directory.insert(END, str(filename))
        file_directory.config(state = DISABLED)
        def_file_path_popup()

# checks if the default file directory is valid
def default_file_directory():
    GD = open('GUI_Defaults.txt', 'r')
    user_def_dir = GD.read()
    GD.close()
    if os.path.exists(user_def_dir) == False:
        user_def_dir = os.getcwd()
        GD = open('GUI_Defaults.txt', 'w')
        GD.write(user_def_dir)
        GD.close()
        

file_path_text = Label(File_info_frame, text = 'Directory of File Output: ')
file_path_text.grid(column = 0, row = 0)

default_file_directory()
GD = open('GUI_Defaults.txt', 'r')
folder_path = GD.read()
GD.close()

file_directory = Entry(File_info_frame)
file_directory.insert(END, str(folder_path))
file_directory.config(state = DISABLED)
file_directory.grid(column = 0, row = 1, ipadx = 100, columnspan = 3)
file_browse_button = Button(File_info_frame, text = 'Browse', 
                            command = browse_directory)
file_browse_button.grid(column = 4, row = 1, padx = 5)

spacer_text = Label(File_info_frame, text = ' ')
spacer_text.grid(row = 2, column = 0)

cmd_file_name_text = Label(File_info_frame, text = 'Command File Name: ')
cmd_file_name_text.grid(column = 0, row = 3)
cmd_file_name = Entry(File_info_frame)
cmd_file_name.grid(row = 3, column = 1)

rad_file_name_text = Label(File_info_frame, text = 'RAD File Name: ')
rad_file_name_text.grid(column = 0, row = 4)
rad_file_name = Entry(File_info_frame)
rad_file_name.grid(row = 4, column = 1)

#------------------------------------------------------------------------------
# Notification Box

Notification_frame = LabelFrame(root, text = 'Notifications', padx = 5,
                                pady = 5)
Notification_frame.grid(row = 0, column = 3, padx = 10, pady = 10, rowspan = 4,
                        columnspan = 3)

Notifications = tkst.ScrolledText(Notification_frame, width = 35, height = 37)
Notifications.pack()
Notifications.insert(INSERT,'Developed by Brandon Staton')
Notifications.insert(INSERT,'\nfor the UAH Astronomy Club')
Notifications.insert(INSERT, '\n\nThis program is a work in progress')
Notifications.insert(INSERT, '\n-----------------------------------\n')
Notifications.config(state = 'disabled')

#-----------------------------------------------------------------------------
# Program info box
Program_info_frame = LabelFrame(root, text = 'Program Info', padx = 5,
                                pady = 5)
Program_info_frame.grid(row = 3, column = 1, padx = 10, pady = 10,)

def open_help():
    current_file_path = str(os.getcwd())
    current_file_path = current_file_path.replace('\\','/')
    help_file_path = current_file_path + '/help_pdf.pdf'
    wb.open_new(help_file_path)
    print(help_file_path)

# Temp text
version_text = Label(Program_info_frame, text = 'Prerelease Version 0.1.1 \n Last updated: July 31, 2020')
version_text.grid(column = 0, row = 0, padx = 5, pady = 5)

help_but = Button(Program_info_frame, text = 'Help Document', command = open_help)
help_but.grid(column = 0, row = 1, padx = 5, pady = 5)


#------------------------------------------------------------------------------
# Validation Functions
global error_string
error_string = ''
global cmd_file_path
global rad_file_path
global cmd_file_name_no_ext
global rad_file_name_no_ext

# Command file name can only consist of numbers, letters, and underscores
def cmd_file_validation():
    nammed_cmd_file = str(cmd_file_name.get())
    cmd_file_direct = str(file_directory.get())
    valid = True
    if nammed_cmd_file == '':
        global error_string
        valid = False
        error_string = error_string + 'Command file name cannot be empty. \n\n'
    else:
        if re.match('^[A-Za-z0-9_]*$', nammed_cmd_file):
            valid = True
            
            global cmd_file_path
            global cmd_file_name_no_ext
            cmd_file_name_no_ext = nammed_cmd_file
            cmd_file_path = cmd_file_direct + '\\' + nammed_cmd_file + '.cmd'
            
            
            if os.path.isfile(cmd_file_path) == True:
                valid = False
                error_string = error_string + 'There is already a command file with that name.\n\n'
            else:
                valid = True

        else:
            valid = False
            error_string = error_string + 'Command file name can only consist of letters, numbers, and underscores. \n\n'
    return valid

# .RAD file name can only consist of numbers, letters, and underscores
def rad_file_validation():
    nammed_rad_file = str(rad_file_name.get())
    rad_file_direct = str(file_directory.get())
    valid = True
    if nammed_rad_file == '':
        global error_string
        valid = False
        error_string = error_string + 'RAD file name cannot be empty. \n\n'
    else:
        if re.match('^[A-Za-z0-9_]*$', nammed_rad_file):
            valid = True
            
            global rad_file_path
            global rad_file_name_no_ext
            rad_file_name_no_ext = nammed_rad_file
            rad_file_path = rad_file_direct + '\\' + nammed_rad_file + '.rad'
            
            if os.path.isfile(rad_file_path) == True:
                valid = False
                error_string = error_string + 'There is already a RAD file with that name.\n\n'
            else:
                valid = True

        else:
            valid = False
            error_string = error_string + 'RAD file name can only consist of letters, numbers, and underscores. \n\n'
    return valid

# Validate all spinbox entries
def spinbox_validate():
    global error_string
    throw_error = False
    
    # if input method is azel coors, validate az and el inputs
    if object_input_method.get() ==2:
        if str(az_value.get()).isdecimal() == False:
            print('az value is not a number')
            error_string = error_string + 'Azimuth value must be an integer between 0 and 359'
            throw_error = True
        elif int(az_value.get()) > 359 or int(az_value.get()) < 0:
            error_string = error_string + 'Azimuth value must be an integer between 0 and 359'
            throw_error = True
        if str(el_value.get()).isdecimal() == False:
            print('el value is not a number')
            error_string = error_string + 'Elevation value must be an integer between 0 and 90'
            throw_error = True
        elif int(el_value.get()) > 359 or int(el_value.get()) < 0:
            error_string = error_string + 'Azimuth value must be an integer between 0 and 90'
            throw_error = True
    # if input method is gal coors, validate lat and lon inputs       
    if object_input_method.get() == 3:
        lat_string = str(lat_value.get())
        if str(lon_value.get()).isdecimal() == False:
            print('Lon value is not a number')
            error_string = error_string + 'Longitude value must be an integer between 0 and 359'
            throw_error = True
        elif int(lon_value.get()) > 359 or int(lon_value.get()) < 0:
            error_string = error_string + 'Longitude value must be an integer between 0 and 359'
            throw_error = True
        if lat_string[0] != '-':
            print(lat_string)
            if lat_string.isnumeric() == True:
                if int(lat_string) > 90:
                    error_string = error_string + 'Latitude value must be an integer between -90 and 90'
                    throw_error = True
            elif lat_string.isnumeric() == False:
                error_string = error_string + 'Latitude value must be an integer between -90 and 90'
                throw_error = True
        elif lat_string[0] == '-':
            abs_lat_string = lat_string[1:]
            if len(abs_lat_string) == 0:
                error_string = error_string + 'Latitude value must be an integer between -90 and 90'
                throw_error = True
            elif abs_lat_string.isnumeric() == True:
                if int(abs_lat_string) > 90:
                    error_string = error_string + 'Latitude value must be an integer between -90 and 90'
                    throw_error = True
            elif abs_lat_string.isnumeric() == False:
                error_string = error_string + 'Latitude value must be an integer between -90 and 90'
                throw_error = True
    
    # validate center frequency
    if str(frequency_box.get()).isdecimal() == True:
        center_freq = str(frequency_box.get())
        if int(center_freq) < 1301 or int(center_freq) > 1699:
            error_string = error_string + 'Center frequency value must be an integer between 1301 and 1699'
            throw_error = True
    elif str(frequency_box.get()).isdecimal() == False:
       error_string = error_string + 'Center frequency value must be an integer between 1301 and 1699'
       throw_error = True
       
    # validate integration time
    if str(integration_time_box.get()).isdecimal() == False:
       error_string = error_string + 'Integration time value must be an integer greater than 0'
       throw_error = True

    # print(throw_error)
    return throw_error
    
    

#------------------------------------------------------------------------------
# Confirm, Finilize, and exit buttons
global output_string # List containing all output info
output_string = []

def error_time():
    messagebox.showwarning('Error', 'Observation already occuring at that day and time')

def Finalized_error():
    messagebox.showwarning('Error', 'No objects inputted')

# error window
def error_popup():
    global error_string
    messagebox.showwarning('Error', error_string)

# Ask if user is sure about exiting program
def exit_popup():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?\n\nAny unsaved data will be lost.') 
   if response == 1:
       root.destroy()


# What to do when the confirm button is clicked
global file_already_inputted
file_already_inputted = False


def confirm_click(file_already_inputted):
    global error_string
    global cmd_file_path
    global rad_file_path
    global output_string
    
    throw_error = False
    error_string = ''
    cmd_file_path = ''
    rad_file_path = ''
    spinbox_error = spinbox_validate()
    if spinbox_error == True:
        error_popup()
    else:
        obs_date = cal.get_date()
        obs_date = str(obs_date)
        obs_hr = int(hr.get())
        obs_min = int(minute.get())
        obs_sec = int(second.get())
        obs_am_pm = am_pm.get()
        time_validation = time_validator(obs_date, obs_hr, obs_min, obs_sec, obs_am_pm)
        if time_validation == False:
            error_string = error_string + 'Inputted time is not valid.\n\n'
            throw_error = True
        
        if file_already_inputted == False:
            cmd_valid = cmd_file_validation()
            rad_valid = rad_file_validation()
            
            if cmd_valid == True and rad_valid == True:
                file_already_inputted = True
                file_browse_button.config(state = DISABLED)
                cmd_file_name.config(state = DISABLED)
            else:
                throw_error = True
        if throw_error == True:
            error_popup()
        else:
            #TODO - add rad file name to the output string
            object_add(obs_date, obs_hr, obs_min, obs_sec, obs_am_pm)
            output_string.sort()
            RFC.main(output_string)
            
            Notifications.config(state = 'normal')
            Notifications.insert(INSERT, '\nObject Inputted')
            Notifications.config(state = 'disabled')
            Notifications.see('end')
        
        print(output_string)
        
# Reset all buttons
def reset_inputs():
    object_input_method.set(2)
    az_reset = StringVar(root)
    az_reset.set('0')
    el_reset = StringVar(root)
    el_reset.set('0')
    az_value.config(state = NORMAL, textvariable = az_reset)
    el_value.config(state=NORMAL, textvariable = el_reset)
    az_value.config(state = DISABLED)
    el_value.config(state=DISABLED)
    int_validate(az_value, limits = (0,359))
    int_validate(el_value, limits = (0,90))
    
    
    object_input_method.set(3)
    lat_reset = StringVar(root)
    lat_reset.set('0')
    lon_reset = StringVar(root)
    lon_reset.set('0')
    lat_value.config(state = NORMAL, textvariable = lat_reset)
    lon_value.config(state=NORMAL, textvariable = lon_reset)
    lat_value.config(state = DISABLED)
    lon_value.config(state=DISABLED)
    int_validate(lat_value, limits = (-90,90))
    int_validate(lon_value, limits = (0,359))
    
    object_input_method.set(1)
    objectBox.current(0)
    objectBox.config(state = 'readonly')
    
    freq_box_create()
    obs_mode_value.current(0)
    
    integration_time_reset = StringVar(root)
    integration_time_reset.set('1')
    integration_time_box.config(textvariable = integration_time_reset)
    
    calibrate.set(1)
    return

# Clear all stored info
def clear():
    global output_string
    global hr
    global minute
    global second
    
    # outputs and file name reset
    output_string = []
    cmd_file_name = Entry(File_info_frame)
    cmd_file_name.grid(row = 3, column = 1)
    rad_file_name = Entry(File_info_frame)
    rad_file_name.grid(row = 4, column = 1)
    
    # Time reset
    hr_default = StringVar(root)
    hr_default.set(12)
    hr = Spinbox(date_time_frame,from_=1, to=12, width = 3, 
                 textvariable = hr_default, wrap=True)
    hr.grid(row = 1, column = 1)
    
    min_default = StringVar(root)
    min_default.set(00)
    minute = Spinbox(date_time_frame, from_ = 00, to=59, width = 3, format="%02.0f",
                     textvariable = min_default, wrap=True)
    int_validate(minute, limits = (00,59))
    minute.grid(row = 1, column = 2)
    sec_default = StringVar(root)
    sec_default.set(00)
    second = Spinbox(date_time_frame, from_=00, to = 59, width = 3, format="%02.0f",
                     textvariable = sec_default, wrap=True)
    int_validate(second, limits = (00,59))
    second.grid(row = 1, column = 3)
    
    # date reset
    time_now = datetime.now()
    current_year = int(time_now.year)
    current_month=int(time_now.month)
    current_day=int(time_now.day)
    cal = Calendar(date_time_frame, selectmode='day',year=current_year,month=current_month,
                    day=current_day, mindate=today)
    cal.grid(row = 0, column = 0, padx = 31, columnspan = 5)
    
    
    


def Finalize():
    # TODO - after cmd and rad files have been written, clear everyting for new file inputs
    global output_string
    if len(output_string) == 0:
        Finalized_error()
        print('Empty')
    else:
        output_string.sort()
        GD = open('GUI_Defaults.txt', 'r')
        user_def_dir = GD.read()
        GD.close()
        write_file = str(user_def_dir) + ' ' + cmd_file_name_no_ext + ' ' + rad_file_name_no_ext
        output_string.insert(0, write_file)
        print(output_string)
        MW.main(output_string)
        Finalize_button.config(state = DISABLED)
        confirm_button.config(state = DISABLED)
        
        Notifications.config(state = 'normal')
        Notifications.insert(INSERT, '\nCommand file being written')
        Notifications.config(state = 'disabled')
        
        # TODO - Do the following only after command file has been
        Notifications.config(state = 'normal')
        Notifications.insert(INSERT, '\nCommand file written\n\n')
        Notifications.config(state = 'disabled')
        Notifications.see('end')
        Finalize_button.config(state = NORMAL)
        confirm_button.config(state = NORMAL)
        reset_inputs()
        clear()
        
    
def object_add(date, hr, mn, sc, AP):
    global output_string
    current_object = ''
    
    # Make month and the day always 2 digits
    inputted_date = date.split('/')
    year = '20' + str(inputted_date[2])
    month = inputted_date[0]
    if int(month) < 10:
        month = '0'+str(month)
    else:
        month = str(month)
    day = inputted_date[1]
    if int(day) < 10:
        day = '0'+str(day)
    else:
        day = str(day)
    current_object = year + '-' + month + '-' + day + ' '
    
    # Convert hours to 24
    if hr == 12 and AP == 'AM':
        hr = 0
    if hr !=12 and AP == 'AM':
        hr = hr
    if hr !=12 and AP == 'PM':
        hr = hr+12
    if hr ==12 and AP == 'PM':
        hr = 12

    # Make minutes, hours, and seconds always 2 digits
    if hr < 10:
        hr = '0' + str(hr)
    if mn < 10:
        mn = '0' + str(mn)
    if sc < 10:
        sc = '0' + str(sc)
    current_object = current_object + str(hr) + ':' + str(mn) + ':' + str(sc) + ' '
    
    # Determine if object defined by coordinates or name
    if object_input_method.get() == 1:
        selected_obj = str(objectBox.get())
        current_object = current_object + 'Listed ' + selected_obj + ' '
        comf_message = '\n' + str(selected_obj) + ' added to file'
        
    elif object_input_method.get() == 2:
        azi = int(az_value.get())
        if azi < 100 and azi > 9:
            azi = '0' + str(azi)
        elif azi < 10:
            azi = '00' + str(azi)
        elif azi >= 100:
            azi = str(azi)
        ele = int(el_value.get())
        if ele < 10:
            ele = '0' + str(ele)
        elif ele > 9:
            ele = str(ele)
        current_object = current_object + 'Azel ' + azi + ':' + ele + ' '
        comf_message = '\nAzel coordinates added to file'
    
    # lat variable is the longitude and lon variable is the latitude
    elif object_input_method.get() == 3:
        lon = int(lon_value.get())
        if lon < 10:
            lon = '00'+ str(lon)
        elif lon > 9 and lon < 100:
            lon = '0' + str(lon)
        else:
            lon = str(lon)
        lat = int(lat_value.get())
        if lat < 0:
            lat = abs(lat)
            if lat < 10:
                lat = '-0' + str(lat)
            else:
                lat = '-' + str(lat)
        elif lat >=0 and lat < 10:
            lat = '0' + str(lat)
        else:
            lat = str(lat)
        current_object = current_object + 'Gal ' + lat + ':' + lon + ' '
        comf_message = '\nGalactic coordinates added to file'
        
    # pass the center frequency to the output
    cent_freq = frequency_box.get()
    current_object = current_object + cent_freq + ' '
    
    # pass the observation mode to the output
    observation_mode = obs_mode_value.get()
    current_object = current_object + observation_mode + ' '
    
    # pass the integration time to the output
    integration_time = integration_time_box.get()
    current_object = current_object + integration_time + ' '
    
    # pass the auto calibration variable to the output
    cal_time = calibrate.get()
    current_object = current_object + str(cal_time) + ' '
    
    # pass the rad file name to the output
    current_object = current_object + str(rad_file_name_no_ext)
    
    # Show user confirmation
    Notifications.config(state = 'normal')
    Notifications.insert(INSERT, comf_message)
    Notifications.config(state = 'disabled')
    Notifications.see('end')
    
    if len(output_string) == 0:
        output_string.append(current_object)
    else:
        # Check if there is already an observation set for that specific time
        date_of_my_input = current_object[0:19]
        for i in range (len(output_string)):
            current_observation_object = output_string[i]
            if date_of_my_input == current_observation_object[0:19]:
                error_time()
                break
            else:
                i = i+1
            if i == len(output_string):
                output_string.append(current_object)
    
    reset_inputs()
    return

# Confirm Object button
confirm_button = Button(root, text = 'Confirm Object',
                        command = lambda: confirm_click(file_already_inputted))
confirm_button.grid(row = 999, column = 3, padx = 5, pady = 5)

# All objects inputted
Finalize_button = Button(root, text = 'Finalize', command = Finalize)
Finalize_button.grid(row = 999, column = 4, padx = 5, pady = 5)


# Exit button
exit_button = Button(root, text = 'Exit', command = exit_popup)
exit_button.grid(row = 999, column = 5, padx = 5, pady = 5)


mainloop()


# TODO - allow user to input multiple rad file names for different observations
# TODO - better checking of time overlap [include integration time]
# TODO - at startup, ask user if they want to delete files that all observations has passed
# TODO - add error if subsequent observations > 24 hours between eachother [ask user to create multiple files]
