# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:37:02 2019

@author: Declan
"""

import TellieTime
import CentreFrequencyAndMode as CFAM
import TelescopePointer as TP
import TimeAndDataPoints as TDP
import FileDictionary2 as FD
import ActualWriterTM as AWTM
def Main():
    '''
    Main function that has all the needed functions in it
    starts user interface
    '''
    objectdict={}#creating the object dictionary
    date=TellieTime.main()#calls the function that asks user for current date and time and converts it into telescope date/time
    objectdict=TP.pointatobject(objectdict)#calls the function that asks user for objects to observe
    freqdict=CFAM.frequencysetter(objectdict)#note that the freqdict keys are flipped wrt objectdict keys
    #don't need a type of calibration function b/c our telescope only has noisecal 
    timerdict=TDP.timeranddatapoints(objectdict)#calls the function that asks users for observation times 
    filenamesdict=FD.filenames(objectdict)#calls the function that asks users for filenames and directories for saving file to 
    print(date)
    print(objectdict)
    print(freqdict)
    print(timerdict)
    print(filenamesdict)
    AWTM.ActualWriterTM(date, objectdict, freqdict, timerdict, filenamesdict)
    return
Main()