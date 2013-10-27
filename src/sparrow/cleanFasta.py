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
        
        if not count % 1000:
            print count;
        
        if count == 2374232:
            nonStandard.append(seqRecord);
            break;
        
        #some may be lowercase
        #sequence=str(seqRecord.seq).upper()        
        
        #if any((c not in ACCEPTABLE_CHARS) for c in sequence):
        #    nonStandard.append(seqRecord)
        
        #for c in sequence:
        #   if(c not in ACCEPTABLE_CHARS):
        #        print seqRecord.id + ": " + c
        
        #if ":" in sequence:
        #    print seqRecord.id
            
    SeqIO.write(nonStandard, outFileName, "fasta")



if __name__ == '__main__':
    listNonStandard(*sys.argv[1:])