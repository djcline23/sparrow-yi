#!/usr/bin/env python

'''
Created on Sept 20, 2013

@author: djcline
'''

import sys
import csv


def reciprocals(firstBlastFileName, secondBlastFileName, outFileName):
    """Finds recriprocal best matches in two blast result files
    with formatting 'qseqid sseqid qlen slen length pident'
    and copies the lines that are reciprocally matched in
    firstBlastFileName into outFileName"""

    with open(firstBlastFileName) as firstBlast, open(secondBlastFileName) as secondBlast, open(outFileName, 'w') as outFile:
        #Make dictionary from query sequence to target sequence from the first blast file
        firstReader = csv.reader(firstBlast)
        firstSecondMap = {row[0] : row[1] for row in firstReader}
        
        #now walk through the second blast file and when we find a match, print that line out
        secondReader = csv.reader(secondBlast)
        count = 0;
        for row in secondReader:
            #Reciprocal by switching columns 0 and 1 of first blast
            if row[0] == firstSecondMap.get(row[1], None):
                outFile.write(",".join(row) + "\n")
                count += 1
        
        print count, 'reciprocal matches'
        
    
    

if __name__ == '__main__':
    reciprocals(*sys.argv[1:])
    
    
    