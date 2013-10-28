#!/usr/bin/env python

'''
Created on Oct 24, 2013

@author: djcline
'''

import sys
from Bio import SeqIO

ACCEPTABLE_CHARS = set('ABCDEFGHIKLMNPQRSTUVWXYZ');

def listNonStandard(inFileName, outFileName):
    """Prints all sequences found in inFile with non standard characters into outFileName"""
    
    #All records which contain nonstandard characetrs
    nonStandard = []
    count = 0;

    for seqRecord in SeqIO.parse(inFileName, "fasta"):
        count += 1;
        
        #some may be lowercase
        sequence=str(seqRecord.seq).upper()        
        
        if any((c not in ACCEPTABLE_CHARS) for c in sequence):
            nonStandard.append(seqRecord)

            
    SeqIO.write(nonStandard, outFileName, "fasta")



if __name__ == '__main__':
    listNonStandard(*sys.argv[1:])