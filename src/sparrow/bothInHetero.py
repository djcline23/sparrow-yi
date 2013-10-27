#!/usr/bin/env python

'''
Created on Oct 20, 2013

@author: djcline
'''

import sys
import csv


def bothInHetero(firstCandFileName, secondCandFileName, checkFileName, outFileName):
    """Includes rows from checkFileName where the first column is in
    firstCandFileName and the second column is in secondCandFileName"""

    with open(firstCandFileName) as firstCands, open(secondCandFileName) as secondCands, open(checkFileName) as checkFile, open(outFileName, 'w') as outFile:
        #Make list of transcript names from the two candidate files
        firstReader = csv.reader(firstCands)
        firstList = {row[0] for row in firstReader}
        
        secondReader = csv.reader(secondCands)
        secondList = {row[0] for row in secondReader}
        
        #now walk through the check file       
        checkReader = csv.reader(checkFile) 
        count = 0;
        for row in checkReader:
            #Reciprocal by switching columns 0 and 1 of first blast
            if row[0] in firstList and row[1] in secondList:
                outFile.write(",".join(row) + "\n")
                count += 1
        
        print count, 'entries where each transcript is found in heterozygote'
        

        
    
    

if __name__ == '__main__':
    bothInHetero(*sys.argv[1:])
    
    
    