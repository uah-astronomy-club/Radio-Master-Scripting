# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:28:34 2020

@author: Brandon Staton
"""

def cmdfilewrite(cmd_file_dir,cmd_name):
    
    
    
    
    
    
    
    full_cmd_file_path = cmd_file_dir + '\\' + cmd_name + '.txt'
    cmdfile = open(full_cmd_file_path,'w+')
    
    
    
    
    
    return

def main():
    test_cmd_file_dir = 'C:\\Users\\bstat\\Documents\\GitHub\\Radio-Master-Scripting\\GUI\\Scripts'
    test_cmd_name = 'testcmd'
    cmdfilewrite(test_cmd_file_dir, test_cmd_name)
main()


#------------------------------------------------------------------------------
# Cmd file format:
#
# [Calibration Time]
# freq [center frequency] [mode]
# test
# noisecal
# [observation time]
# record [rad file name]
# [observation] roff
# stow