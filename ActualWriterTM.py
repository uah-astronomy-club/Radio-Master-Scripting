# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:19:34 2019

@author: Declan
"""

def ActualWriterTM(Date,Objects,Frequencies,Times,Filenames):
    '''
    Takes the date formatting, the dictionary of objects, the dictionary of frequencies,
    the dictionary of times, and the dictionary of filenames
    formatting is assumed to be like:
    writes the .cmd file in the proper formatting 
    '''
    #TODO - Sort by soonest to be observed to latest before writting cmd file
    #TODO - if time between last data point of object n and start of data collecting for n+1 is >20 mins, stow telecope
    with open(Filenames['directoryname']+'/'+Filenames['filename']+'.txt','w+') as cmdfile:   
        cmdfile.write(Date+'\n')
        for Object in Objects.keys():
            freq=0#initiates var
            mode=0
            f=Frequencies.keys()
            if 'all' in f:
                s=Frequencies['all']
                s=s.split(',')
                freq=s[0]
                mode=s[1]
            else:
                s=Frequencies[Object]
                s=s.split(',')
                freq=s[0]
                mode=s[1]
            cmdfile.write(': freq '+freq+' '+mode+'\n')
            if Objects[Object]=='named':
                cmdfile.write(': '+Object+'\n')
            elif Objects[Object]=='Galactic':
                cmdfile.write(': galactic '+Object+'\n')#check to make sure this comes out in the correct format
            elif Objects[Object]=='Azel':
                cmdfile.write(': azel '+Object+'\n')#check to make sure this comes out in the correct format
            n=Filenames[Object]
            cmdfile.write(": record"+' '+n+".rad\n")
            t=Times.keys()
            if 'all' in t:
                s=Times['all']
                s=s.split(',')
                inter=s[0]
                cmdfile.write(": "+inter+'\n')
            else:
                s=Times[Object]
                s=s.split(',')
                inter=s[0]
                cmdfile.write(":"+inter+'\n')
            cmdfile.write(": roff\n")
        cmdfile.write(": stow")
    #for object
    #set freq and mode 
    #point at the object
    #start datafile
    #insert time for integration
    #stop data file
    #calibrate telescope if needed
    #next object 
    return 