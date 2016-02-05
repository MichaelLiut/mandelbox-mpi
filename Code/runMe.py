#!/usr/bin/env python
def runScript():
	import subprocess
	import sys
	import os

	# 2200 to 2250
	for i in range (0 , 7200):
		np = sys.argv[1]
		n = str(i)
                if i <= 9:
                    filenameDAT = 'params' + n.rjust(5-len(n),'0') + '.dat'
                elif i <= 99:
                    filenameDAT = 'params' + n.rjust(6-len(n),'0') + '.dat'
                else:
                    filenameDAT = 'params' + n.rjust(7-len(n),'0') + '.dat'
		bashCommand = "mpirun -np " + np + " ./mandelbox " + filenameDAT + ';'
		os.system(bashCommand)
runScript()
		
