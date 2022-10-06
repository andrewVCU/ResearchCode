"""
Created on Wed Oct 5 2022

@author: Andrew Hale
"""
import argparse

parser = argparse.ArgumentParser(description="Count and return list of shared hits between Blast outputs")
parser.add_argument('--file1', type=str, required=True, help="First Accession List")
parser.add_argument('--file2', type=str, required=True, help="Second Accession List")
parser.add_argument('--outfile', type=str,required=True, help="Name of out file")
args = parser.parse_args()

accList1 = []
sharedCount = 0

with open(args.file1, 'r') as infile1:
    for line in infile1:
        accList1.append(line)
infile1.close()

with open(args.file2, 'r') as infile2:
    lines = infile2.readlines()
    outLines = []
    outLines.append("Shared Hits: ")
    total = len(lines)
    progCount = 0
    outfile = open(args.outfile, 'w')
    for line in lines:
        if line in accList1:
            if line not in outLines:
                outLines.append(line)
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
infile2.close()
