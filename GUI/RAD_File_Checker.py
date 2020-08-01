# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:27:19 2020

@author: Brandon Staton

Error is either True or False
location is the index of the rad file between subsequent uses of the same rad file name
"""

def main(output_string):
    error = False
    rad_files = []
    i=0
    # Get the rad file names
    while i < len(output_string):
        current_object = output_string[i].split()
        rad_files.append(current_object[8])
        i = i+1
    print(rad_files)
    
    
    if len(rad_files) > 2:
        j = 0
        while j < (len(rad_files)-2):
            current_data_file_name = rad_files[j]
            bracket_data_file_name = rad_files[j+2]
            if current_data_file_name == bracket_data_file_name:
                if rad_files[j+1] != current_data_file_name:
                    error = True
                    location = j+1
            j = j+1
    return error,location
    
    

test_string = ['2020-08-01 00:00:00 Listed 10G 1301 1 1 1 rad1', '2020-08-02 00:00:00 Listed 10G 1301 1 1 1 rad2', '2020-08-01 00:00:00 Listed 10G 1301 1 1 1 rad1']
throw_error = main(test_string)[0]
location = main(test_string)[1]
print(throw_error,location)