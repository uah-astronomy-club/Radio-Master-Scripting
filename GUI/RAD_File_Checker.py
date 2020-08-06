# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:27:19 2020

@author: Brandon Staton

Error is either True or False
location is the index of the rad file between subsequent uses of the same rad file name
"""

def main(output_string):
    location = 0
    error = False
    rad_files = []
    err_rad = ''
    bracket_data_file_name = ''
    brckt_rad = ''
    i=0
    # Get the rad file names
    while i < len(output_string):
        current_object = output_string[i].split()
        rad_files.append(current_object[8])
        i = i+1
    
    
    if len(rad_files) > 2:
        j = 0
        while j < (len(rad_files)-2):
            current_data_file_name = rad_files[j]
            bracket_data_file_name = rad_files[j+2]
            if current_data_file_name == bracket_data_file_name:
                if rad_files[j+1] != current_data_file_name:
                    brckt_rad = bracket_data_file_name
                    err_rad = rad_files[j+1]
                    error = True
                    location = j+1
            j = j+1
    if error == True:
        del output_string[location]
    return error,output_string,err_rad,brckt_rad
    
    

# test_string = ['2020-08-01 00:00:00 Listed 10G 1301 1 1 1 rad1']
# #               , '2020-08-02 00:00:00 Listed 10G 1301 1 1 1 rad2', '2020-08-01 00:00:00 Listed 10G 1301 1 1 1 rad1']
# throw_error,output,invalid_rad,current_rad = main(test_string)
# print(throw_error)
# print(output)
# print(invalid_rad)
# print(current_rad)