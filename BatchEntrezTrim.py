# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:52:48 2022

@author: awhal
"""

def dictCreate(fileName):
    entryNum = -1
    with open(fileName,'r') as infile:
        numOrgDict = {}
        lines = infile.readlines()
        for line in lines:
            line = line.split("\t")
            if len(line) > 1:
                numOrgDict[lines[entryNum].strip()] = line[0] + "\t" + line[3].strip()
            entryNum += 1
        infile.close()
        return numOrgDict

def EditBlastOut(IDandOrgDict, fileName):
    tempLine = ""
    with open(fileName, 'r') as infile: 
        outfile = open("NotTheCreekWTaxonNamesTest.out",'w')
        data = infile.readlines()
        i = 0
        for line in data:
            if not line:
                pass
            tempLine = line.split()
            tempNum = tempLine[1]

            if tempNum in IDandOrgDict:
                organism = IDandOrgDict[tempNum].split()[1]
                data[i] = data[i].strip("\n") + "\t" + organism + "\n"
            i += 1
        outfile.writelines(data)
        infile.close()
        outfile.close()
                
EditBlastOut(dictCreate("NotTheCreekHitsWtaxonomy2.txt"), "NotTheCreekFilteredHits.out")   
#./TestingData/