# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:21:09 2022

@author: awhal
"""
"""
for each gene number, find the top viral hit, and top bacterial hit based on 
% ident
"""
phageName = "NotTheCreek_"

def splitting(fileName):
    outfile = open("topHitsTesting.out",'w')
    infile = open(fileName)
    lineList = infile.readlines()
    infile.close()
    
    geneNum = 0
    line = 0
    lineCount = 0
    for elm in lineList:
        line = elm.split("\t")
        if geneNum == 0:
            geneNum = line[0]
        elif line[0] != geneNum:
            lineList.insert(lineCount,'\n')
            geneNum = line[0]
        lineCount+=1
        
    newContents = "".join(lineList)
    outfile.write(newContents)
    outfile.close()

def HighestBactOrVirus(fileName):
    with open(fileName, "r") as infile:
        highestBact = 0
        highestVir = 0
        current = 0
        highestBactString = ""
        highestVirString = ""
        BestHitsList =[]

        for line in infile:
            if line == "\n":
                if highestBactString:
                    highestBactString = highestBactString.replace(phageName,"")
                    BestHitsList.append(highestBactString)
                if highestVirString:
                    highestVirString = highestVirString.replace(phageName,"")
                    BestHitsList.append(highestVirString)

                highestBact = 0
                highestVir = 0
                current = 0
                highestBactString = ""
                highestVirString = ""
            
            line = line.split()
            if not line:
                continue
            elif len(line) != 13:
                continue
            
            current = float(line[2])
            if line[12] == "BCT":
                if current > highestBact:
                    highestBact = current
                    highestBactString = "\t".join(line)
            elif line[12] == "PHG":
                if current > highestVir:
                    highestVir = current
                    highestVirString = "\t".join(line)
            elif line[12] == "ENV":
                continue
                    
        if highestBactString:
            highestBactString = highestBactString.replace(phageName,"")
            BestHitsList.append(highestBactString)
        if highestVirString:
            highestVirString = highestVirString.replace(phageName,"")
            BestHitsList.append(highestVirString)
        
        outfile = open("NotTheCreek_TopHitsBactVirusTest.out",'w')
        newContents = "\n".join(BestHitsList)
        outfile.write(newContents)
        infile.close()
        outfile.close()

splitting("NotTheCreekWTaxonNames.out") 
HighestBactOrVirus("topHitsTesting.out")