# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:33:48 2020

@author: Brandon Staton
"""
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
root=Tk()
root.title('UAH Astronomy Club')
root.geometry('500x500')

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
    print(object_input_method_value)

# Defining the buttons
Bt1 = Radiobutton(object_frame, text = 'Listed', variable = object_input_method, 
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
        objectBox.config(state = NORMAL) 
objectBox = ttk.Combobox(object_frame, value=content)
objectBox.current(0)
objectBox.bind('<<ComboboxSelected>>',selected)
objectBox.grid(row = 0, column = 1, padx=10)



# #------------------------------------------------------------------------------
# # Current time and date
# time_now = datetime.now()
# current_year = int(time_now.year)
# current_month=int(time_now.month)
# current_day=int(time_now.day)
# current_hr = int(time_now.hour)
# current_min =int(time_now.minute)

# # Time and date picker
# cal = Calendar(root, selectmode='day',year=current_year,month=current_month,
#                day=current_day)
# cal.pack(pady=20)

# def grab_date():
#     obs_date = cal.get_date()
#     print(obs_date)
    
    
# date_confirm_button = Button(root, text = 'Confirm Date', command = grab_date)
# date_confirm_button.pack(pady=20)



mainloop()

'''
Things to add:
    Clock with the current time at the top of this program
    Remove print statements
'''
