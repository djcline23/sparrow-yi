#!/usr/bin/env python

'''
Created on Oct 14, 2013

@author: djcline
'''

import sys
import csv


def lengthFilter(recipFileName, outFileName):
    """Walks through a file of blast reciprocal matches given in recipFileName
    and copies them to outFileName if the length of the query and target transcripts
    are no more than 5% longer than the length of the alignment"""

    with open(recipFileName) as recipFile, open(outFileName, 'w') as outFile:
        reader = csv.reader(recipFile)
        
        count = 0;
        for row in reader:
            alignLen     = int(row[4])
            allowableLen = alignLen * 1.05
            queryLen     = int(row[2])
            targetLen    = int(row[3])
            
            if queryLen <= allowableLen and targetLen <= allowableLen:
                outFile.write(",".join(row) + "\n")
                count += 1
        
        print count, 'results'
        
    
    

if __name__ == '__main__':
    lengthFilter(*sys.argv[1:])