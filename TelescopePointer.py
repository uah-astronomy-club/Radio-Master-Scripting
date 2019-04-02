# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:40:00 2019

@author: Brandon Staton
"""
# Figure out wtf to do with this 'global' list

def pointatobject(dictionary):
    '''
    takes a dictionary and adds various objects per user's input 
    marks the type of input (named,azel, or gal) as the value and the object 
    name/coordinates as the key
    '''
    l_or_c = input("Listed object or Coordinates? ")    #Dont make user input entire word
    
    if (l_or_c.lower() == 'listed'):
        listed_object = input('Name of Object: ')
        #look for listed_object in list before appending
        dictionary.update({listed_object:'named'})
    
    elif (l_or_c.lower() == "coordinates"):
        g_or_a = input("Gal or Azel coordinates? ")
        while True:
            if (g_or_a.lower() == 'gal'):
                while True:
                    gal_lat = int(float(input('Input Galactic Longitude:  ')))
                    if (gal_lat>=0 and gal_lat<=359):
                        if (gal_lat>=0 and gal_lat<=9):     #Makes all inputted numbers 2 digit
                            gal_lat = str('0') + str(gal_lat)
                        gal_lat = str(gal_lat)
                        break
                    else:
                        print('Invalid Input - #todo: add sassy comment')
                while True:
                    gal_lon = int(float(input('Input Galactic Latitude: ')))
                    if (gal_lon>=-90 and gal_lon<=90):
                        neg=False
                        if (gal_lon < 0):   #Makes all inputted numbers 2 digit
                            neg = True
                            gal_lon = abs(gal_lon)
                        if (gal_lon >= 0 and gal_lon <= 9):
                            gal_lon = str('0')+str(gal_lon)
                            if (neg == True):
                                gal_lon = str('-') + gal_lon
                        gal_lon = str(gal_lon)
                        break
                    else:
                        print('Invalid Input')
                gal_coors = gal_lon + ' ' + gal_lat
                dictionary.update({gal_coors:'Galactic'})
                break
            elif (g_or_a.lower() == "azel"):
                while True:
                    Azel_az = int(float(input('Input Azimuth:  ')))
                    if (Azel_az>=0 and Azel_az<=359):
                        if (Azel_az>=0 and Azel_az<=9): #Makes all inputted numbers 2 digit
                            Azel_az = str('0') + str(Azel_az)
                        Azel_az = str(Azel_az)
                        break
                    else:
                        print('Invalid Input, Azimuth must be between 0 and 359')
                while True:
                    Azel_el = int(float(input('Input Elevation:  ')))
                    if (Azel_el>=0 and Azel_el<=90):
                        if (Azel_el>=0 and Azel_el<=9): #Makes all inputted numbers 2 digit
                            Azel_el = str('0') + str(Azel_el)
                        Azel_el = str(Azel_el)
                        break
                    else:
                        print('Invalid Input, Elevation must be between 0 and 90')
                azel_coors = Azel_az + ' ' + Azel_el
                dictionary.update({azel_coors:'Azel'})
                break
            else:
                print("Invalid Input - Sorry. I dont speak wrong.")
                g_or_a = input("Galactic or Azel coordinates? ")
            
    else:
        print("Invalid Input - It is not rocket science")
        pointatobject(dictionary)
    while True:
        new_obj = input('Another object? (Y/N) ')
        if(new_obj.lower() == 'y'):
            pointatobject(dictionary)
            break
        elif(new_obj.lower() == 'n'):   # Sometimes you have to say no twice for program to end. IDK how to fix right now
            #print(dictionary)
            break
        else:
            print("Invalid Input - 1+1=2. I thought you might need help with that as well.")
    return dictionary
# def main() for Testing Purposes Only
'''def main():
    pointatobject()
main()'''
