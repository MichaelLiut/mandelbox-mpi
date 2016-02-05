def runScript():
    import subprocess
    import sys
    import os

    for i in range (0 , 7200):

        n = str(i)

        if i <= 9:
            filenameIN = 'f' + n.rjust(5-len(n),'0') + '.bmp'
            filenameOUT = 'f' + n.rjust(5-len(n),'0') + '.jpeg'
        elif i <= 99:
            filenameIN = 'f' + n.rjust(6-len(n),'0') + '.bmp'
            filenameOUT = 'f' + n.rjust(6-len(n),'0') + '.jpeg'
        else:
            filenameIN = 'f' + n.rjust(7-len(n),'0') + '.bmp'
            filenameOUT = 'f' + n.rjust(7-len(n),'0') + '.jpeg'

        bashCommand = "convert " + filenameIN + " " + filenameOUT
        #print(bashCommand)
        os.system(bashCommand)

runScript()