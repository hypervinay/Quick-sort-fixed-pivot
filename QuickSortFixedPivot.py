import time
import sys

def QuickSortFixedPivot(inputList):
    if len(inputList)>1:
    	pivot = inputList[0];
    	lessthanPivot = [i for i in inputList if i< pivot];
    	equaltoPivot = [i for i in inputList if i==pivot];
    	greaterthanPivot = [i for i in inputList if i> pivot];
    	
	return QuickSortFixedPivot(lessthanPivot) + equaltoPivot + QuickSortFixedPivot(greaterthanPivot)

    else:
	return inputList;

if len(sys.argv)!=3:
	print "Incorrect Format!! Enter [filename].py [input file name] [Output file name]"
	sys.exit();

with open(sys.argv[1],'r') as f:
	inputList = [int(x) for x in f.read().split(',')];

startTime = time.time();
print "Running time = ",time.time()-startTime," secs";
fout = open(sys.argv[2],'w');
print >>fout, QuickSortFixedPivot(inputList);
fout.close();

