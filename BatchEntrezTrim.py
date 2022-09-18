# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:52:48 2022

@author: awhal
"""
import sys

batchEntrez = sys.argv[1]
filteredBlast = sys.argv[2]
organism = sys.argv[3]

def dictCreate(fileName):

    print("---------------------------------------------\nCreating Organism Dictionary: " + batchEntrez +"\n-------------------------------------\n")
    entryNum = -1
    with open(fileName,'r') as infile:
        numOrgDict = {}
        lines = infile.readlines()
        for line in lines:
            line = line.split("\t")
            if len(line) == 4:
                numOrgDict[lines[entryNum].strip()] = line[0] + "\t" + line[3].strip()
            elif len(line) == 3:
                numOrgDict[lines[entryNum].strip()] = line[0] + "\t" + line[2].strip()
            entryNum += 1
        infile.close()
        print("Finished Creating Dictionary\n")
        return numOrgDict

def EditBlastOut(IDandOrgDict, fileName):

    print("---------------------------------------------\nEditing Blast File: " + filteredBlast +"\n---------------------------------------------\n")
    tempLine = ""
    with open(fileName, 'r') as infile: 
        outfile = open(organism +"WithTaxonNames.out",'w')
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
    print("Finished Editing Blast File\n")

EditBlastOut(dictCreate(batchEntrez), filteredBlast)   
