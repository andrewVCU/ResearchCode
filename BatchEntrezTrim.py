# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:52:48 2022

@author: awhal
TODO:
Update to include Argparser for argument passing
"""

import sys
batchEntrez = sys.argv[1]
filteredBlast = sys.argv[2]
outName = sys.argv[3]

"""
batchEntrez = "CP51_BatchEntrez.out"
filteredBlast = "CP51_FilteredBlast.out"
outName = "CP51_Taxon.out"
"""

def dictCreate(fileName):

    print("---------------------------------------------\nCreating Organism Dictionary: " + batchEntrez +"\n-------------------------------------\n")
    entryNum = -1
    with open(fileName,'r') as infile:
        entrezOutNum = 0
        numOrgDict = {}
        lines = infile.readlines()
        for line in lines:
            line = line.split("\t")
            if len(line) == 4:
                numOrgDict[line[0].strip() + ".1"] = line[3]
                entrezOutNum += 1
            elif len(line) == 3:
                numOrgDict[line[0].strip() + ".1"] = line[2]
                entrezOutNum += 1
            entryNum += 1
        infile.close()
        print("Finished Creating Dictionary\n")
        print("There were " + str(entrezOutNum) + " returns from Entrez.")
        return numOrgDict

def EditBlastOut(IDandOrgDict, fileName):

    print("---------------------------------------------\nEditing Blast File: " + filteredBlast +"\n---------------------------------------------\n")
    tempLine = ""
    with open(fileName, 'r') as infile: 
        outfile = open(outName,'w')
        outfile.write("Prot\tID\tPerc\tnull\tnull\tnull\tnull\tnull\tnull\tnull\tnull\tnull\tOrg\n")
        data = infile.readlines()
        i = 0
        for line in data:
            if not line:
                pass
            tempLine = line.split()
            tempNum = tempLine[1]

            if tempNum in IDandOrgDict:
                taxon = IDandOrgDict[tempNum]
                """
                genusA = IDandOrgDict[tempNum].split()[2]
                genusB = genusA.split()[0]
                """
                data[i] = data[i].strip("\n") + "\t" + taxon
            i += 1
        outfile.writelines(data)
        infile.close()
        outfile.close()
    print("Finished Editing Blast File\n")

EditBlastOut(dictCreate(batchEntrez), filteredBlast)

