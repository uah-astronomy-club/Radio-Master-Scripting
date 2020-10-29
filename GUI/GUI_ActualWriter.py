# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:28:34 2020

@author: Brandon Staton
"""

def cmdfilewrite(start,cmd_file_dir,cmd_name,cal_time,cent_freq,mode,new_rad,obs_time,rad_file,object_type,obs_object,int_time,last):
    
    #TODO - change .txt to .cmd
    full_cmd_file_path = cmd_file_dir + '\\' + cmd_name + '.txt'
    if start == True:
        cmdfile = open(full_cmd_file_path,'w+')
        cmdfile.write(cal_time)
        cmdfile.write('\n:freq ' + str(cent_freq) + ' ' + str(mode))
        cmdfile.write('\n:test')
        cmdfile.write('\n:noisecal')
        cmdfile.close()
    
    
    cmdfile = open(full_cmd_file_path,'a')
    cmdfile.write('\n' + str(obs_time))
    
    if new_rad == True:
        cmdfile.write('\n:record ' + str(rad_file))
    
    if object_type == 'Listed':
        object_write = obs_object
    elif object_type == 'Gal':
        object_write = 'galactic ' + str(obs_object)
    elif object_type == 'Azel':
        object_write = 'azel ' + str(obs_object)

    
    cmdfile.write('\n:' + object_write)
    cmdfile.write('\n:' + str(int_time))
    cmdfile.write('\n:roff')
    cmdfile.close()
    
    if last == True:
        cmdfile = open(full_cmd_file_path,'a')
        cmdfile.write('\n:stow')
        cmdfile.close()
    
    
# Everything below here is for testing purposes only and needs removed
    # So I dont have to keep opening the text file
    f = open(full_cmd_file_path,'r')
    file_contents = f.read()
    print(file_contents)
    return

# def main():
#     start = True
#     test_cmd_file_dir = 'C:\\Users\\bstat\\Documents\\GitHub\\Radio-Master-Scripting\\GUI\\Scripts'
#     test_cmd_name = 'testcmd'
#     cal_time = '2020:001:01:00:59'
#     cent_freq = 1400
#     mode = 1
#     obs_time = '2020:001:01:15:59'
#     rad_file = 'testrad.rad'
#     object_type = 'listed'
#     obs_object = 'moon'
#     int_time = 20
    
#     new_rad = True
#     last = True
    
#     cmdfilewrite(start,test_cmd_file_dir, test_cmd_name,cal_time,cent_freq,mode,new_rad,obs_time,rad_file,object_type,obs_object,int_time,last)
# main()

# def test():
#     return


#------------------------------------------------------------------------------
# Cmd file format:
#
# [Calibration Time]
# freq [center frequency] [mode]
# test
# noisecal
#
#
# [observation time]
# record [rad file name]
# [observation]
# [integration time]
# roff
# stow