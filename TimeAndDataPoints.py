# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 21:59:48 2019

@author: Declan
"""

def timeranddatapoints(objectlist):
    '''
    takes a dictionary of objects and uses their keys to assign the length of each data point and how many data points should be taken
    returns a dictionary using the same keys but the values are 'length,number of points' 
    note that if all are using the same lenght the dictionary will be {'all':'length,number of points'}
    
    '''
    timeanddatapointsdict={}
    while True:    
        setall=input('Would you like to enter the same integration settings for all objects you wish to observe?\nEnter yes or no.')
        if setall.lower()=='yes':
            while True:
                p=input("what would you like the integration period to be (in seconds)?")
                try: 
                    p=int(p)
                    if p<1:
                        print('Negative time? NEGATIVE TIME? Really? REALLY? Like, are you sure you want to work in a STEM field?')
                    else:
                        break
                except ValueError:
                    print("You need to enter an integer, come on-it's as easy as 1,2,3.")            
            while True:
                cp=input("how often do you want to calibrate the telescope (in seconds)?")
                try: 
                    cp=int(cp)
                    if cp<1:
                        print('Negative time? NEGATIVE TIME? Really? REALLY? Like, are you sure you want to work in a STEM field?')
                    else:
                        break
                except ValueError:
                    print("You need to enter an integer, come on-it's as easy as 1,2,3.")
            st=str(p)+','+str(cp)
            timeanddatapointsdict.update({'all':st})
            break
        elif setall.lower()=='no':
            for thing in objectlist.keys():
                print('Current object:'+thing)
                while True:
                    p=input("what would you like the integration period to be (in seconds)?")
                    try: 
                        p=int(p)
                        if p<1:
                            print('Negative time? NEGATIVE TIME? Really? REALLY? Like, are you sure you want to work in a STEM field?')
                        else:
                            break
                    except ValueError:
                        print("You need to enter an integer, come on-it's as easy as 1,2,3.")
                while True:
                    cp=input("how often do you want to calibrate the telescope (in seconds)?")
                    try: 
                        p=int(p)
                        if p<1:
                            print('Negative time? NEGATIVE TIME? Really? REALLY? Like, are you sure you want to work in a STEM field?')
                        else:
                            break
                    except ValueError:
                        print("You need to enter an integer, come on-it's as easy as 1,2,3.")
                timeanddatapointsdict.update({thing:str(p)+','+str(cp)})
            break
        else:
            print("You didn't enter yes or no, this is not a hard question-what are you? a biology major?")
    return timeanddatapointsdict