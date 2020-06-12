# -*- coding: utf-8 -*-
"""
GUI_Master_Writer
Created on Fri Jun 12 14:49:38 2020

@author: Brandon Staton
"""
import GUI_TellieTime as TT

def main(objects):
    files_info = objects[0].split()
    directory = files_info[0]
    cmd_file = files_info[1] + '.cmd'
    rad_file = files_info[2] + '.rad'
    
    # Deletes the file directory and name info for easier indexing
    del objects[0]
    for i in range(len(objects)):
        current_object_info = objects[i].split()
        '''
        current_object_info:
            [0] is date
            [1] is time
            [2] is listed/azel/gal
            [3] is object name/ coordinates
            [4] is center freq
            [5] is observation mode
            [6] is integration time
            [7] is time between calibrations
        '''
        corrected_date = TT.main(current_object_info[0], current_object_info[1])
        
        
        
        
        print(corrected_date)
        
        
        print(current_object_info)
    return

main(['C:/Users/bstat/Documents/GitHub/Radio-Master-Scripting/GUI cmd rad', 
      '2020-12-31 19:02:03 Listed 40G 1301 1 1 0'])