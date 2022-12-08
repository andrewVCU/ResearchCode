"""
Created on Wed Dec 7 2022

@author: Andrew Hale
"""
import argparse

parser = argparse.ArgumentParser(description="Label Bin Region Queries With Their Functions")
parser.add_argument('--inFile', type=str, required=True, help="Bin File")
parser.add_argument('--functions', type=str, required=True, help="Feature Table for Functions")
parser.add_argument('--outfile', type=str,required=True, help="Name of out file")
args = parser.parse_args()

with open(args.functions, 'r') as functFile:
    functDict = {}
    func = ""
    num = ""
    temp = ""
    split = []
    for line in functFile:
        if ">" in line:
            if func != "" and num != "":
                functDict[num] = func
                func = ""
                num = ""

            split = line.split("|")
            num = split[1]
        if "product" in line and func == "":
            temp = line.strip()
            func = temp.replace("product\t", "")
    functFile.close()

outfile = open(args.outfile, 'a')
outfile.write("Query\tCount\tFunction\n")
with open(args.inFile) as binFile:
    lines = binFile.readlines()
    for line in lines:
        split = line.split()
        num = split[0]
        if num in functDict:
            outfile.write(line.strip() + "\t" + functDict[num] + "\n")
    outfile.close()
    binFile.close()
