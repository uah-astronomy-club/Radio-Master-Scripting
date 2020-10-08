# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:50:37 2019

@author: Declan
"""
def main(objectlist):
    '''
    Input: dictionary of objects w/ obj name as the key
    Return: dict of {object name:'frequency,mode'}
    '''
    frequencydict={}
    
    
    
    return














# Orignal code
#==============================================================================
# def frequencysetter(objectlist):
#     '''
#     takes a dictionary of objects with the name of the object as the key
#     returns a dictionary of {object name:'frequency,mode'}, note that the dictionary is in reverse order from the input dictionary
#     if one frequency the key is: 'all'
#     '''
#     frequencydict={}
#     while True:    
#         setall=input('Would you like to enter the same frequency settings for all objects you wish to observe?\nEnter yes or no. ')
#         if setall.lower()=='yes':
#             while True:
#                 freq=input('Enter the centring frequency in MHz from 1301 to 1799 MHz: ')
#                 if not (1300<float(freq)<1800):     # Changed to include 1300 and 1800 MHz
#                     print("That's outside the telescope's measuring range of 1300-1800 MHz" )
#                 else:
#                     break
#             while True:   
#                 mode=input('Enter the mode (1,2,3,4) you want to observe in: ')
#                 List=[1,2,3,4]
#                 if int(mode) not in List:
#                     print('That is not a valid observing mode! Maybe you should stick to binoculars...')
#                 else:
#                     frequencydict.update({'all':freq+','+mode})
#                     break
#             break
#         elif setall.lower()=='no':
#             for thing in objectlist.keys():
#                 print("Current object:"+thing)#note that this expects the key to be a string
#                 while True:
#                     currentfreq=input('Enter the centring frequency for the current object from 1300 to 1800 MHz: ')
#                     if not (1300<=float(currentfreq)<=1800):
#                         print("That's outside the telescope's measuring range of 1300-1800 MHz.")
#                     else:
#                         break
#                 while True:
#                     currentmode=input('Enter the mode (1,2,3,4) you want to observe in: ')
#                     List=[1,2,3,4]
#                     if int(currentmode) not in List:
#                         print('That is not a valid observing mode! Maybe you should stick to binoculars...')
#                     else:
#                         frequencydict.update({thing:currentfreq+','+currentmode})#note that this epects the key to be a string
#                         break
#             break
#         else:
#             print("You didn't enter yes or no, this is not a hard question-what are you? a biology major?")
#     return frequencydict
