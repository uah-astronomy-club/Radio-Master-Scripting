# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:13:01 2018

@author: Declan
"""
import calendar #Calendar file from the internet: https://www.guru99.com/calendar-in-python.html
from datetime import datetime # Used for Year error handeling
def TellieTime(Day,Month,Year,Time,M):
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
    if M=='PM': #checks if the time is afternoon b/c we need to convert to military before adjusting to universal
        if Time[0:2]=='12': #checks if it's noon b/c we don't need a military conversion
            if isDaylightSavings(Year, Month, Day)==False: 
                Th=int(Time[0:2])+6
            else:
                Th=int(Time[0:2])+5
        elif len(Time)==4: #checks if the hour is single digits
            if isDaylightSavings(Year, Month, Day)==False:  
                Th=int(Time[0])+18 #adds 12 to convert to military then 6 to universal
            else:
                Th=int(Time[0])+17 #adds 12 to convert to military then 5 to universal
        else: #this should run the above if/else for double digit hours
            if isDaylightSavings(Year, Month, Day)==False: #checks for daylightsavings 
                Th=int(Time[0:2])+18
            else:
                Th=int(Time[0:2])+17
    else: #means time is in am & we can just add
        if len(Time)==4: #checks if the hour is single digits 
            if isDaylightSavings(Year, Month, Day)==False: #checks for daylightsavings 
                Th=int(Time[0])+6
            else:
                Th=int(Time[0])+5
        else: #this should run the above if/else for double digit hours
            if isDaylightSavings(Year, Month, Day)==False: #checks for daylightsavings 
                Th=int(Time[0:2])+6
            else:
                Th=int(Time[0:2])+5
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
    
    if len(Time)==4: #checks if hour is single or double digit as it affects the indexing
        Ti=str(Th)+Time[1:4]
    else:
        Ti=str(Th)+Time[2:5]
    d=str(d)
    Year=abs(Year)
    y=str(Year)
    print(y+':'+d+':'+Ti+':00') #prints the formatted stuff for error checking
    return (y+':'+d+':'+Ti+':00')

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
    
# HELLO DECLAN ITS BRANDON
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

# Function that uses the datetime library to determine the current year
def current_year():
    time_now = datetime.now()
    current_year = int(time_now.year)
    return current_year
def current_month():
    time_now=datetime.now()
    current_month=int(time_now.month)
    return current_month
def current_day():
    time_now=datetime.now()
    current_day=int(time_now.day)
    return current_day
# Makes values easier to enter for the user
def main():
    print("Input the following information about your observation")
    
    # Prompts the user for the year
    inpt_year = int(float(input("Year: ")))
    while (inpt_year < current_year()):
        inpt_year = int(float(input("Input valid year: ")))
    
    # Gets Month input
    monthint = int(float(input("Month Number: ")))
    while (monthint < 1 or monthint > 12):      # Checks if inputted integer is between 1 and 12
        monthint = int(float(input("Input Valid Month: ")))
    while (monthint<current_month()):
        monthint=int(float(input("Input Future Month:")))
    # Gets the day of the month and does simple error handeling
    day = int(float(input("Day of the Month: ")))
    while (day < 1 or day > 31):
        day = int(float(input("Input valid day: ")))
    while((monthint==9 or monthint==4 or monthint==6 or monthint==11)and day > 30):
        day = int(float(input("Input valid day: ")))
    while((monthint==2 and isLeapYear(inpt_year) == True) and day>29):
        day = int(float(input("Input valid day: ")))
    while((monthint==2 and isLeapYear(inpt_year) == False) and day>28):
        day = int(float(input("Input valid day: ")))
    while(day<current_day() and monthint==current_month()):
        day=int(float(input("Input Future Day: ")))
    time = str(input("12 hr time (hr:mn): "))
    
    AM_PM = str(input("AM or PM (all caps): "))
    print(" ")
    date=TellieTime(day,monthint,inpt_year,time,AM_PM)
    print(" ")


    # Included so the program can be run in a command window without closing to quickly for user to see the result
    #end = input('Press Enter to end program')
    return date
# Starts Function
if __name__ == "__main__":
    main()
