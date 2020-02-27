'''
GraphRadio.py
Description: Reads data from .rad radio data files and produces a graph along
             with a statistics file regarding the data.
Author: Nicholas Schragal
Last Modified: 2018-10-24
'''

import matplotlib.pyplot as plt
import csv
#   User inputs directory where files to be processed are

fileDirectory = input("Type the directory the files to be processed are found in-use "+'\\'*2+ "\n>>")

#   The user can input multiple directories one at a time, but it will only 
#   process in one directory at a time

while fileDirectory != "done":
    if fileDirectory[len(fileDirectory)-1] != '/':
        fileDirectory += '/' 
        
    print("You entered: " + fileDirectory)
    txtfileDirectory=input("Type the directory the stat files are to be stored in-use "+'\\'*2+ "\n>>")
    graphfileDirectory=input("Type the directory the graphs are to be stored in-use "+'\\'*2+ "\n>>")
    #   The user can input multiple files found in the previously input
    #   directory to be processed in turn.
    
    fileNames = []
    
    fileNameInput = input("Type the names of the files to be processed in that directory, include the file extension. Type \"done\" once you have put in all the file names\n>>")
    
    while fileNameInput != "done":
        fileNames.append(fileNameInput)
        print("You entered: " + fileNameInput)
        fileNameInput = input("Type another file name, type \"done\" once finished\n>>")
    
    
    
    #   Processing each data file in turn
    
    for fileName in fileNames:
        
        #   First, trying to open the file, if it fails to open, it indicates
        #   an error has occurred and moves on to the next file to try to open
        
        try:
            with open(fileDirectory + fileName, "r") as inputFile:
                print("Processing " + fileName)
                inputLines = inputFile.readlines()
        
        except FileNotFoundError:
            print("Can't find file " + fileName)
            continue
        
        #   Cutting off the file extension from the file and saving the name
        #   of the file as a new string
        
        nameOfFile = fileName.split('.')[0]
        
        #   Declaring two lists, one that will contain the sums of each
        #   frequency bin, the second contians the values of the frequencies
        
        binSums = []
        frequencies = []
        
        #   Initializing the binSums and frequencies arrays with zeroes
        #   for the binSums and the frequencies for the frequencies array
        
        for index in range(0, 156):
            binSums.append(0.0)
            frequencies.append(index + 1)
        
        #   Now it processes each line in the file
        
        for line in inputLines:
            
            #   If the line starts with an asterisk, it means it's a comment
            #   line and should be ignored in the processing
            
            if (line[0] == '*'):
                print("Skipped a comment line in " + fileName)
            
            #   Otherwise, it's a data line and needs to be parsed
            
            else:
                
                #   The line's values are split into a list, where the
                #   delimiter is a space
                
                partsOfLine = line.split()
                
                #   The actual data values we want are now added to the binSums
                #   list, to get the sum of each bin over the integrated period
                
                for i in range(0, 156):
                    try:
                        binSums[i] += float(partsOfLine[i+9])
                    except ValueError:
                        continue 
                
        #   Printing a message to indicate that the file has been processed
        
        print(fileName + " processed successfully")
        
        #   Now, starting to construct a string to be printed to a statistics
        #   file that describes the data in the raw file more concisely
        
        statsString = "*Sums of bins:\n"
        
        #writes the values as a massive string
        for value in binSums:
            statsString += str(value)
            statsString += ","
        #   Opening the statistics file and printing the statistics string to
        #   it
        try:
            with open(txtfileDirectory + '/' + nameOfFile + "stats.txt", "w+") as statsFile:
                statsFile.write(statsString)
        
        #   If it fails to open, it prints an error message 
        
        except FileNotFoundError:
            print("Can't create statistics file for " + fileName)
            continue
        
        #   Closing the statistics file object
        
        statsFile.close()
        #creating a .csv file of stats
        Header=True
        with open(txtfileDirectory+'/'+nameOfFile+"stats.txt",newline='') as In_File:#opens the stats.txt file that ws just created
            data=csv.reader(In_File,delimiter=',')
            for row in data: 
                if Header==True:#checks for header and skips it
                    Header=False
                else:
                    Datapoints=row#the way the .txt files are there's only 2 rows, once past the first one the next row is all the data points
            Datapoints.remove('') #for some reason there's a space at the end of the file, this gets that out of there so we don't get a str->float error
            for init in Datapoints: 
                Datapoints[Datapoints.index(init)]=round(float(init),1) #turns each datapoint into a float w/ 1 digit past the decimal
        #writing data back into the file 
        Fname=nameOfFile+"stats.csv"
        with open(txtfileDirectory+'/'+Fname,'w') as Writeto: #creates the .csv file
            writeto=csv.writer(Writeto,delimiter=',')#creates the writer
            writeto.writerow(Datapoints)#writes the data points, each one seperated by a comma
        #   Now plotting a figure with the binSums list, flux (which really
        #   isn't flux at this time, it's antenna temperature) vs. frequency
        
        plt.figure(1)
        plt.subplot(1, 1, 1)
        plt.title("Frequencies vs. Flux")
        plt.xlabel("Frequencies")
        plt.ylabel("Flux")
        plt.plot(frequencies, binSums)
        plt.tight_layout()
        plt.savefig(graphfileDirectory + '/'+ nameOfFile + ".pdf")
        plt.close()
        
        #   Printing a message stating that the data plot has been generated
        
        print(fileName + " plot generated")
        
    fileDirectory = input("Type another file directory, type \"done\" once finished\n>>")