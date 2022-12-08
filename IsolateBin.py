"""
Created on Mon Oct 10 2022

@author: Andrew Hale
"""
import argparse

parser = argparse.ArgumentParser(description="Return the hits within a desired bin of the frequency plots")
parser.add_argument('--inFile', type=str, required=True, help="Hit File")
parser.add_argument('--min_percid', type=str, required=True, help="Lower Bound")
parser.add_argument('--max_percid', type=str,required=True, help="Upper Bound")
parser.add_argument('--outfile', type=str,required=True, help="Name of out file")
args = parser.parse_args()

min = args.min_percid
max = args.max_percid
outfile = open(args.outfile, 'a')
ID_CountDict = {}
dictCount = 0
outLines = []
with open(args.inFile, 'r') as infile:
    outfile.write("List of Queries Within Bin Range: " + args.min_percid +
        " - " + args.max_percid + "\n\n")
    outfile.write("Query\tCount\n")
    for line in infile:
        splitLine = line.split()
        id = splitLine[0].strip()
        percid = splitLine[2]
        if id == "Prot":
            continue
        if len(splitLine) < 13:
            continue
        if(float(percid)>=float(min) and float(percid)<=float(max)) and splitLine[12] == "BCT":
            if id not in outLines:
                ID_CountDict[id] = 1
                outLines.append(id)
            else:
                ID_CountDict[id] += 1
        dictCount += 1

    for key, value in ID_CountDict.items():
        outfile.write('%s\t%s\n' % (key, value))

    outfile.close()
    infile.close()

