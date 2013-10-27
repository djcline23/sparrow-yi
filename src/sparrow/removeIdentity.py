#!/usr/bin/env python

'''
Created on Oct 14, 2013

@author: djcline
'''

import sys
import csv


def removeIdentity(recipFileName, outFileName):
    """Walks through a file of blast reciprocal matches given in recipFileName
    and copies them to outFileName unless the length of the query and target transcripts
    are the same length as the alignment and the percent identity is 100"""

    with open(recipFileName) as recipFile, open(outFileName, 'w') as outFile:
        reader = csv.reader(recipFile)
        
        count = 0;
        for row in reader:
            queryLen     = row[2]
            targetLen    = row[3]
            alignLen     = row[4]
            percIdentity = row[5]            
            
            if not (queryLen == alignLen and targetLen == alignLen and percIdentity == "100.00"):
                outFile.write(",".join(row) + "\n")
                count += 1
        
        print count, 'results'
        
    
    

if __name__ == '__main__':
    removeIdentity(*sys.argv[1:])