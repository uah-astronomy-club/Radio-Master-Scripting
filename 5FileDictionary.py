#Mason Alfonso
# I don't know what special treatment objects need, I just know init is a thing

def dictAppend ():

        # here is the dictionary with the directory, cmdfile, and object stuff its supposed to contain, left objects vague because I wasn't sure what was going in here        
        fileDict = {'mainDirectory':'blank'}

        for value in list(fileDict.items()): #for loop that should iterate through every value in the dictionary.
                                             # the list(dict) is in there because python didn't like having the values changed while the for loop was iterating through the dictionary             

                fileDict[value] = str(input('++input the file name into your computer\n')) # the plus signs were/are there so I could test the while loop
                while(True): # ye "error handling" is in this while loop.  It doesn't really do anything except encourage the user to put better inputs in if they screw up.  Nothing fancy
                        
                        try:

                                open(fileDict[value], 'r') #tries to read the file, seems harmless to do
                                print(fileDict[value]) # ERROR CHECKING!!! This line can be deleted, it's just useful when testing the program
                        except FileNotFoundError:
                                         
                                
                                print('Spirited attempt!  Not quite what this program wants though, try again\n')
                                fileDict[value] = str(input('Input the file location\n'))
                        else:
                                break
                                
        print(fileDict[value])  
        return(fileDict) #not 100% sure on the syntax here but its easy to change

dictAppend()
#fileDict = {'mainDirectory':'blank', 'cmdFile':'blank', 'objectOne':'blank','objectTwo':'blank','objectThree':'blank'}

                             

