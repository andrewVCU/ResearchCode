"""
Created on Wed Oct 5 2022

@author: Andrew Hale
"""
import argparse

parser = argparse.ArgumentParser(description="Count and return list of shared hits between Blast outputs")
parser.add_argument('--file1', type=str, required=True, help="First Blast Output")
parser.add_argument('--file2', type=str, required=True, help="Second Blast Output")
parser.add_argument('--outfile', type=str,required=True, help="Name of out file")
args = parser.parse_args()

accList1 = []
accList2 = []
sharedCount = 0

with open(args.file1, 'r') as infile1:
    for line in infile1:
        newLineA = line.split("\t")

        #One entry in accList = [Query_Prot, Hit]
        accList1.append(newLineA)
infile1.close()

with open(args.file2, 'r') as infile2:
    for line in infile2:
        newLineA = line.split("\t")

        #One entry in accList = [Query_Prot, Hit]
        accList2.append(newLineA)
infile2.close()


outLines = []
outLines.append("Shared Hits: " +"\n")
outLines.append("Query1\tQuery2\tMatch\n")

total = len(accList1)
progCount = 0
outfile = open(args.outfile, 'w')
for pairA in accList1:
    for pairB in accList2:
        if pairA[1] == pairB[1]:
            addLine =  pairA[0] +"\t"+ pairB[0] +"\t"+ pairA[1] + "\n"
            if addLine not in outLines:
                outLines.append(addLine)
                sharedCount += 1
    #Progress tracker
    progCount += 1
    percentComplete = (progCount/total)*100
    perString = "Counting: " + str(round(percentComplete))
    print("%s%%"%perString, end = "\r")
outLines[0] = "Shared Hits: " + str(sharedCount) + "\n"
outfile.writelines(outLines)
outfile.close()
print("File1 and File2 share "+str(sharedCount)+" hit(s).")
