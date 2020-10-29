# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:31:44 2020

@author: Brandon Staton
"""

def starttime(obs_time):
    '''
    This program determines the time at which start the calibrtaion of
    the telescope before the data observations begin
    '''
    year = obs_time[0:4]
    year = int(year)
    
    day = obs_time[5:8]
    day = int(day)
    
    hr = obs_time[9:11]
    hr = int(hr)
    
    mn = obs_time[12:14]
    mn = int(mn)
    
    sc = obs_time[15:17]
    sc = int(sc)
    
    # Make sure if 15 mintues are taken from the given time, resulting time is valid
    if mn < 15:
        if hr == 0:
            if day == 0 and isLeapYear(year - 1) == True:
                year = year - 1
                day = 365
            elif day==0 and isLeapYear(year-1)==False:
                year = year-1
                day = 364
            else:
                day = day-1
            hr = 23
        else:
            hr = hr-1
        mn = mn+60
    
    # do the 15 minute subtract
    mn = mn-15
    
    # do the formatting and return the value
    year = str(year)
    if sc < 10:
        sc = '0'+str(sc)
    else:
        sc = str(sc)
    
    if mn < 10:
        mn = '0' + str(mn)
    else:
        mn = str(mn)
    
    if hr<10:
        hr = '0' + str(hr)
    else:
        hr = str(hr)
    
    if day < 100:
        if day < 10:
            day = '00'+str(day)
        else:
            day = '0'+str(day)
    else:
        day = str(day)       
                  
    calibration_time = year + ':' + day + ':' + hr + ':' + mn + ':' + sc
    print(calibration_time)
 
    #TODO - check if day light savings before deleting hour
    return calibration_time

def isLeapYear(year):
    # Var that holds True if year is leap year and False if not a leap year
    Leap_year = False
    #Is year evenly divisible by 4
    if year % 4 == 0:
    
        #if year is evenly divisible by 4, checks if year is evenly divisible by 100
        if year % 100 == 0:
        
            #If year is evenly divisible by 4 and 100, checks if year is evenly divisible by 400
            if year % 400 == 0:
                Leap_year = True
            else:
                Leap_year = False
        else:
            Leap_year = True
    else:
        Leap_year = False
    return Leap_year