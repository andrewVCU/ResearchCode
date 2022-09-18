import os
import sys

#Initial inputs

#Used for pullProtIDs
protFasta = sys.argv[1]

#Raw blast return
allHits = sys.argv[2]

#Organism Name used for file naming
orgName = sys.argv[3]

def pullProtIDs(fasta):
    #Pulls the protein IDs for recognizing a self hit
    print("---------------------------------------------\nRunning pullProtIDs on: " + protFasta +"\n---------------------------------------------\n")
    with open(fasta, 'r') as infile:
        lines = infile.readlines()
        total = len(lines)
        progCount = 0
        for line in lines:
            if '>' in line:
                splitLine = line.split(" ")
                protID = splitLine[0].replace(">","")
                protID=protID.replace("\n","")
                outfile = open(orgName+"_Prots.txt",'a')
                outfile.write(protID + "\n")

            progCount += 1
            percentComplete = (progCount/total)*100
            perString = "Pulling Protein IDs: " + str(round(percentComplete))
            print("%s%%"%perString, end = "\r")
            
        print("\n")
        print("Self Protein IDs Pulled\n")
        return outfile.name

def blastFilter(selfProts, allHits):
    print("---------------------------------------------\nRunning blastFilter on: " + allHits +"\n---------------------------------------------\n")
    percentComplete = 0
    with open(allHits, 'r') as infile:
        lines = infile.readlines()
        total = len(lines)
        progCount = 0
        repeatCheck = []
        for line in lines:
            lineTemp = line.split("\t")   
            protList = open(selfProts, 'r')
            protIDs = protList.readlines()
            prot = lineTemp[1] + "\n"
            if prot in protIDs:
                continue
            #if accession doesnt meet starting criteria for a self hit
            else:
                eVal = float(lineTemp[10])
                percIdent = float(lineTemp[2])

                #define an out for the filtered
                outfile = open(orgName+"_FilteredBlast.out", 'a')

                #add to entrez list and filtered blast
                batchEntrez = open(orgName + "BatchEntrezList.txt",'a')
                if eVal <= 1.0E-7 and percIdent >= 30.00:
                    outfile.write(line)
                    accNum = lineTemp[1]
                    if accNum in repeatCheck and len(repeatCheck) > 0:
                        continue
                    else:
                        repeatCheck.append(accNum)
                        batchEntrez.write(accNum + "\n")
                        
            #Progress tracker
            progCount += 1
            percentComplete = (progCount/total)*100
            perString = "Filtering: " + str(round(percentComplete))
            print("%s%%"%perString, end = "\r")

    print("\n")
    print("Blast Filtered")

    #Self Proteins
    protList.close()
    os.remove(protList.name)

    #filtered blast
    outfile.close()

    #All hits file
    infile.close()

    #List of accession nums for batch entrez
    batchEntrez.close()


print("======================\nB L A S T  F I L T E R\n======================\n" + 
      "Blast File:    " + allHits + "\n" +
      "Protein Fasta: " + protFasta + "\n" + 
      "Organism:      " + orgName + "\n")

blastFilter(pullProtIDs(protFasta), allHits)