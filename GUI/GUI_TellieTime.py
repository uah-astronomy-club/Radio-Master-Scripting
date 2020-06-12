# -*- coding: utf-8 -*-
"""
GUI_TellieTime
Created on Fri Jun 12 16:25:11 2020

@author: Brandon Staton
"""

import calendar #Calendar file from the internet: https://www.guru99.com/calendar-in-python.html
from datetime import datetime # Used for Year error handeling
def TellieTime(Day,Month,Year,Hr,Mn,Sc):
    """
    Day/Year are pretty obivious, just put in the number
    Month must be spelled correctly & Capitalized 
    Time should be given in 12-hour 12:00 format and needs to be a string
    M is the AM/PM marker, needs to be a str and in all caps 
    """ 
    #comment test
    if isLeapYear(Year) == True: #checks if leap year
        if Month==1:
            Dadjust=0
        elif Month==2:
            Dadjust=31
        elif Month==3:
            Dadjust=60
        elif Month==4:
            Dadjust=91
        elif Month==5:
            Dadjust=121
        elif Month==6:
            Dadjust=152
        elif Month==7:
            Dadjust=182
        elif Month==8:
            Dadjust=213
        elif Month==9:
            Dadjust=244
        elif Month==10:
            Dadjust=274
        elif Month==11:
            Dadjust=305
        elif Month==12:
            Dadjust=335
    # the following adjusts the day value for the month if not a leap year
    else:
        if Month==1:
            Dadjust=0
        elif Month==2:
            Dadjust=31
        elif Month==3:
            Dadjust=59
        elif Month==4:
            Dadjust=90
        elif Month==5:
            Dadjust=120
        elif Month==6:
            Dadjust=151
        elif Month==7:
            Dadjust=181
        elif Month==8:
            Dadjust=212
        elif Month==9:
            Dadjust=243
        elif Month==10:
            Dadjust=273
        elif Month==11:
            Dadjust=304
        elif Month==12:
            Dadjust=334
    d=Day+Dadjust #gets day as the number of the day in the year
    
    if Hr == 12: # If time is noon, Th is known
        if isDaylightSavings(Year, Month, Day) == False:
            Th = 18
        else:
            Th = 17
    else: # If time is not noon, add 5 or 6 hours to convert to universal time
        if isDaylightSavings(Year, Month, Day) == False:
            Th = Hr + 6
        else:
            Th = Hr + 5
    
    if Th>=24: #if our time conversion has put us past midnight in universal time, we need to change the date
        Th-=24
        d+=1

    # Year Incriment rewritten to take into account leap year or not
    if isLeapYear(Year) == True and d>=367:
        d-=366
        Year+=1
    elif isLeapYear(Year) == False and d>=366:
        d-=365
        Year+=1
    
    # Formatting of the day output
    if d < 10:
        d = '00'+str(d)
    elif d > 9 and d < 100:
        d = '0'+str(d)
    else:
        d = str(d)
    
    # Formatting of the hour output
    if Th < 10:
        Th = '0'+str(Th)
    else:
        Th = str(Th)
    
    # Formatting of the minute output
    if Mn < 10:
        Mn = '0'+str(Mn)
    else:
        Mn = str(Mn)
    
    # Formatting of the seconds output
    if Sc < 10:
        Sc = '0'+str(Sc)
    else:
        Sc = str(Sc)
    
    
    Year=int(Year)
    y=str(Year)
    # print(y+':'+d+':'+Th + ':' + Mn + ':' + Sc) #prints the formatted stuff for error checking
    return (y+':'+d+':'+Th+':' + Mn + ':' + Sc)

# Daylight savings helper function
def isDaylightSavings(Year, Month, Day):
    '''
    Takes the date and uses it to check if daylight savings is on
    at the date entered, returns a boolean (True if it is daylight savings (March-November))
    Month should be in numberical format (ie: June=6)
    '''
    if (Month<3) or (Month==12): #if it's before March or after November you're always out of Daylight savings
        return False
    if (Month !=3) & (Month !=11): #if March<Month<November it's definitly Daylight savings 
        return True
    C=calendar.monthcalendar(Year,Month) #forms a base calender of the month/year
    c=C[0] #grabs the list of the days of the first week 
    c2=C[1] #grabs the list of the days of the second week
    FirstSunday=c[calendar.SUNDAY] #tells the day number that the first sunday occurs on 
    SecondSunday=c2[calendar.SUNDAY] #tells the day number that the second sunday occurs on 
    if Month==11: #if it's November
        if Day<FirstSunday: #if it's before the first Sunday of November Daylight savings is still on
            return True
        else:
            return False
    elif Month==3: 
        if Day<SecondSunday: #if it's before the second Sunday of March Daylights savings is still off 
            return False
        else:
            return True
    
# Leap year program
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


# Splits the time and date into indivudial variables for easier use
def main(date, time):
    date_info = date.split('-')
    inpt_year = int(date_info[0])
    monthint = int(date_info[1])
    day = int(date_info[2])
    
    time_info = time.split(':')
    obs_hr = int(time_info[0])
    obs_min = int(time_info[1])
    obs_sec = int(time_info[2])
    
    date=TellieTime(day,monthint,inpt_year,obs_hr,obs_min,obs_sec)
    return date

    
# For testing purposes only
if __name__ == "__main__":
    date = '2020-12-31'
    time = '19:02:03'
    main(date, time)