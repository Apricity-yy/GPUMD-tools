#!/usr/bin/python
'''
script to repick xyz from cp2k-pos* for every 10 or 20 structure.
use:python mdsimplify.py n(n is every n numbers extract one structure)
'''
import sys,math,linecache

inputFile = "NEP-dataset.xyz"
#inputFile = "cp2k-pos-1.xyz"
numOfAtoms = (linecache.getline(inputFile,1)).strip()
N = int(numOfAtoms) + 2
print 'number of Atoms:', int(numOfAtoms)

count = -1
for count, line in enumerate(open(inputFile, 'rU')):
    pass
count += 1
print count

O = (count//N)/int(sys.argv[1])
print O

Output = open('train1.xyz','w')
for i in range(0,O):
    for j in range(1,N+1):
		print >> Output,(linecache.getline(inputFile,i*int(sys.argv[1])*N+j)).strip()


