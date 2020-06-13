# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:40:00 2019

@author: Brandon Staton
"""
def pointatobject(dictionary, input_method, object_pos):
    '''
    takes a dictionary and adds various objects per user's input 
    marks the type of input (named,azel, or gal) as the value and the object 
    name/coordinates as the key
    '''
    if input_method == 'Listed':
        dictionary.update({object_pos:'named'})
    elif input_method == 'Gal':
        object_pos = object_pos.replace(':', ' ')
        dictionary.update({object_pos:'Galactic'})
    else:
        object_pos = object_pos.replace(':',' ')
        dictionary.update({object_pos:'Azel'})
    return dictionary

# def main() for Testing Purposes Only
# def main():
#     print(pointatobject({},'Azel',  '001:01' ))
# main()
