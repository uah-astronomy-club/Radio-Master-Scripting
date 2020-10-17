# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:02:22 2019

@author: Declan
"""
import os #Used to check if there is already a file with the specified name

def filenames(objectdict):
    '''
    takes a dictionary of objects to be observed
    asks where the .cmd files are to be stored and what the .rad files should be called
    returns a dictionary w/ keys of the directory and the objects w/ values of the names
    '''
    filenamesdict={}
    while True:
        default_dir = 'C:/Users/bstat/Documents/GitHub/Radio-Master-Scripting/GUI'
        yn = input('Use default file path of ' + default_dir + ' ? y/n: ')
        if (yn=='y'):
            dictoryname = default_dir
        else:
            dictoryname=input("Enter the file directory to write the .cmd files to (don't need '' or ""): ")
        filenamesdict.update({'directoryname':dictoryname})
        cmdfileoverride = False
        while (cmdfileoverride == False):
            cmdname=input("Enter the name for the .cmd file: ")
            if (os.path.isfile(dictoryname +'/'+ cmdname +'.txt') == True):
                override = input('cmd file already exists. Override (y/n)?: ')
                if (override == 'y'):
                    cmdfileoverride = True
            else:
                cmdfileoverride=True
                
        
        filenamesdict.update({'filename':cmdname})
        break
    for thing in objectdict:
        while True:
            print('Current object: '+thing)
            objectstr=input('Enter what you want the .rad file for the current object to be named: ')
            #TODO - add check if .rad file already exists
            #TODO - add default file name based on time of observation. ex. moon_2020_01_27(1)
            #need fix to prevent spaces 
            try:
                objectstr=str(objectstr)
                filenamesdict.update({thing:objectstr})
                break
            except ValueError:
                print("You're like the Kardashians-unable to name anything")
    return filenamesdict
        