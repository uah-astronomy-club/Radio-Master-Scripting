# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:50:37 2019

@author: Declan
"""
def main(i,freq,mode):
    '''
    Input: dictionary of objects w/ obj name as the key
    Return: dict of {object name:'frequency,mode'}
    '''
    frequencydict={}
    
    # makes all keys 2 characters
    if int(i)< 10:
        i = '0' + str(int(i))
        
    freq = str(freq)
    mode = str(mode)
    
    frequencydict.update({i:freq+','+mode})
    return frequencydict