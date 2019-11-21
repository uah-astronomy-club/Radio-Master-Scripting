# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:02:22 2019

@author: Declan
"""

def filenames(objectdict):
    '''
    takes a dictionary of objects to be observed
    asks where the .cmd files are to be stored and what the .rad files should be called
    returns a dictionary w/ keys of the directory and the objects w/ values of the names
    '''
    filenamesdict={}
    while True:
        dictoryname=input("Enter the file directory to write the .cmd files to (don't need '' or "")")
        filenamesdict.update({'directoryname':dictoryname})
        cmdname=input("Enter the name for the .cmd file")
        filenamesdict.update({'filename':cmdname})
        break
    for thing in objectdict:
        while True:
            print('Current object'+thing)
            objectstr=input('Enter what you want the .rad file for the current object to be named')
            #need fix to prevent spaces 
            try:
                objectstr=str(objectstr)
                filenamesdict.update({thing:objectstr})
                break
            except ValueError:
                print("You're like the Kardashians-unable to name anything")
    return filenamesdict
        