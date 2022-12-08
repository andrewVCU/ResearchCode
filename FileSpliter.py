# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:35:55 2022
 
@author: awhal
"""
import sys
seqNum = 0
seqlim = 100
fileNum = 1
smallFile = None

input = sys.argv[1]
name = sys.argv[2]

with open(input,'r') as infile:
    smallFilename = name + '_{}.fa'.format(fileNum)
    smallFile= open(smallFilename,"w")
    for line in infile:
        if line.startswith('>'):
            if seqNum > seqlim:
                if smallFile:
                    smallFile.close()
                    fileNum += 1
                    seqNum = 0
                smallFilename = name + '_{}.fa'.format(fileNum)
                smallFile= open(smallFilename,"w")
            seqNum += 1
            smallFile.write(line)
        else:
            smallFile.write(line)       
        
      
                
            
            