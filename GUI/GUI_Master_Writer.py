# -*- coding: utf-8 -*-
"""
GUI_Master_Writer
Created on Fri Jun 12 14:49:38 2020

@author: Brandon Staton
"""
import GUI_TellieTime as TT
import GUI_TelescopePointer as TP
import GUI_CentFreqMode as CFM
import GUI_TimeAndDataPoints as TDP
import GUI_FileStart as FS
#import GUI_ActualWriter as AW

def main(objects):
    files_info = objects[0].split()
    directory = files_info[0]
    cmd_file = files_info[1] + '.cmd'
    
    # Deletes the file directory and name info for easier indexing
    del objects[0]
    for i in range(len(objects)):
        current_object_info = objects[i].split()
        object_dictionary = {}
        
        # Convert inputted date to year:day:hr:mn:sc
        corrected_date = TT.main(current_object_info[0], current_object_info[1])
        corrected_date = str(corrected_date)
        print(corrected_date)
        
        if i==1:
            calibration_time = FS.starttime(corrected_date)
            start = True
        else:
            start = False
        
        if i == len(objects):
            last = True
        else:
            last = False
            
        # Puts all objects to be observed in a dictionary
        object_dictionary = TP.pointatobject(object_dictionary, 
                                             current_object_info[2], 
                                             current_object_info[3])
        
        # Sends the info to center frequ
        freq_info = CFM.main(i,current_object_info[4], current_object_info[5])
        
        #Sends info to time and data points
        #timer_dict = TDP.timeanddatapoints(object_dictionary, 
        #                                     current_object_info[6])
        
        #Send all the info to the program that writes the command file
        
        
        
        
        
        '''
        current_object_info:
            [0] is date
            [1] is time
            [2] is listed/azel/gal
            [3] is object name/ coordinates
            [4] is center freq
            [5] is observation mode
            [6] is integration time
            [7] is auto calibration yes/no (1/2)
            [8] is rad file name
        '''
        
        
        print('\n\nGUI_Master_Writter Opened\n')
        print(corrected_date)
        print(current_object_info)
        print('Object Dict: ' + str(object_dictionary))
    return

#['2020-10-15 00:00:00 Listed 40G 1301 1 1 1 rad', '2020-10-16 00:00:00 Listed 60G 1304 2 2 2 rad2']
#['C:\\Users\\bstat\\Documents\\GitHub\\Radio-Master-Scripting\\GUI cmd rad2', '2020-10-15 00:00:00 Listed 40G 1301 1 1 1 rad', '2020-10-16 00:00:00 Listed 60G 1304 2 2 2 rad2']


main(['C:\\Users\\bstat\\Documents\\GitHub\\Radio-Master-Scripting\\GUI cmd', '2020-10-15 00:00:00 Listed 40G 1301 1 1 1 rad', '2020-10-16 00:00:00 Listed 60G 1304 2 2 2 rad2'])

# add integration time to observation start time to determine observation end time


'''
2020:356:18:00:00
{'moon': 'named'}
{'all': '1440,1'}
{'all': '20,40'}
{'directoryname': 'C:/Users/bstat/Documents/GitHub/Radio-Master-Scripting/GUI', 'filename': 'testcmd', 'moon': 'testrad'}
'''

