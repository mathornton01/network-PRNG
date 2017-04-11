from csv import *
from itertools import cycle
import statistics


def bs2hs(bs):
	hs = ''
	nybblesz = len(bs)/4
	bitNumb=0
	for i in range(0,int(nybblesz)): 
		nybble = bs[bitNumb] + bs[bitNumb+1] +bs[bitNumb+2] +bs[bitNumb+3]
		bitNumb = bitNumb + 4
		hs = hs + hex(int(nybble,2))[2:]
	return hs


time = []

with open('nehaCapLarge.csv') as micFile: 
    fprs = reader(micFile,delimiter=',',quotechar='\"')
    for row in fprs:
        time.append(row[1])

#Remove the header information

time = time[1:len(time)+1]
loop = True

curidx = 0

td = []
print(len(time))
for i in range(0,len(time)-1,1):
    # Check to see if you are out of range
    if i == len(time)-1:
        break
    else:
        td.append(float(time[i+1]) - float(time[i]))

MOC = statistics.median(td)

rs = ''

for item in td: 
    if item > MOC:
        rs = rs + '1'
    else:
        rs = rs + '0'

#print(bs2hs(rs))
