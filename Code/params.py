#!/usr/bin/env python
import sys

def main():
    camX = 15
    camY = 0
    camZ = 0
    lookX = 0
    lookY = 0
    lookZ = 0
    upY = 1
    upX = 0
    upZ = 0

    # For final : double = 2, half = 0.5
    # For testing : double = 1, half = 1
    double = 2
    half = 0.5

    for i in xrange(0 * double, 3610 * double):
    	if i < (200 * double):
    		camX = camX - (0.047 * half)		#camX = 5.6
    		camY = camY + (0.019 * half)	    #camY = 3.8
    		camZ = camZ + (0.0185 * half)		#camZ = 3.7
    		lookX = lookX + (0.018 * half)		#lookX = 3.6
    		lookY = lookY + (0.019 * half)		#lookY = 3.8
    		lookZ = lookZ + (0.0185 * half)		#lookZ = 3.7
    	elif i < (212 * double):
    		camX = camX - (0.01 * half)			#camX = 3.48
    	elif i < (260 * double):
    		camX = camX + (0.01 * half)			#camX = 6.08
        	camY = camY + (0.01 * half)			#camY = 4.28
    		camZ = camZ - (0.01 * half)			#camZ = 3.22
        elif i < (400 * double):			
        	camX = camX - (0.01 * half)			#camX = 4.68
        elif i < (600 * double):
        	camX = camX - (0.01 * half)			#camX = 2.68
        	lookX = lookX - (0.01 * half)		#lookX = 1.6
        	lookY = lookY + (0.0024 * half)		#lookY = 3.8
        	lookZ = lookZ - (0.0024 * half)		#lookZ = 3.7
        elif i < (665 * double):
            camX = camX - (0.01 * half)          #camX = 2.03
            lookX = lookX - (0.02 * half)        #lookX = 0.30
            lookZ = lookZ - (0.02 * half)        #lookZ = 2.40
        elif i < (725 * double):
            camX = camX - (0.01 * half)          #camX = 1.43
            camZ = camZ - (0.005 * half)         #camZ = 2.92
            lookX = lookX - (0.02 * half)        #lookX = -0.9
            lookZ = lookZ - (0.02 * half)        #lookZ = 1.2
        elif i < (750 * double):
            camX = camX - (0.005 * half)         #
            camZ = camZ - (0.005 * half)         #
            lookX = lookX - (0.02 * half)        #
            lookZ = lookZ - (0.02 * half)        #
        elif i < (775 * double):
            camX = camX - (0.005 * half)         #
            camZ = camZ - (0.005 * half)         #
            lookX = lookX + (0.01 * half)        #
            lookZ = lookZ - (0.02 * half)        #
        elif i < (850 * double):
            camZ = camZ - (0.005 * half)         #
            lookX = lookX + (0.02 * half)        #
            lookZ = lookZ - (0.02 * half)        #
        elif i < (900 * double):
            camZ = camZ - (0.005 * half)         #
            lookX = lookX + (0.03 * half)        #
            lookZ = lookZ - (0.03 * half)        #
        elif i < (950 * double):
            camX = camX + (0.001 * half)
            camZ = camZ - (0.005 * half)         #
            lookX = lookX + (0.03 * half)        #
            lookZ = lookZ - (0.03 * half)        #
        elif i < (1030 * double):
            camX = camX + (0.001 * half)
            camZ = camZ - (0.005 * half)         #
            lookX = lookX + (0.03 * half)        #
            lookZ = lookZ - (0.03 * half)        #
        elif i < (1075 * double):
            camX = camX + (0.001 * half)
            camZ = camZ - (0.005 * half)         #
            lookX = lookX + (0.03 * half)        #
            lookZ = lookZ + (0.03 * half)        #
        elif i < (1100 * double):
            camX = camX + (0.001 * half)
            camZ = camZ - (0.005 * half)        #
            lookX = lookX + (0.05 * half)        #
            lookZ = lookZ + (0.05 * half)        #
        elif i < (1200 * double):
            lookX = lookX + (0.05 * half)        #
            lookZ = lookZ + (0.05 * half)        #
        elif i < (1250 * double):
            lookX = lookX + (0.05 * half)        #
            lookZ = lookZ + (0.05 * half)        #
            lookY = lookY - (0.1 * half)
        elif i < (1280 * double):
        	lookY = lookY - (0.05 * half)
        	camX = camX + (0.05836 * half)
        	camZ = camZ + (0.0075 * half)
        elif i < (1400 * double):
        	lookX = lookX + (0.1 * half)
        	lookZ = lookZ + (0.1 * half)
        elif i < (1460 * double):
        	lookY = lookY + (0.065 * half)
        	lookZ = lookZ - (0.1 * half)
        	lookX = lookX - (0.1 * half)
        	camX = camX + (0.01 * half)
        	camZ = camZ + (0.005373882 * half)
        elif i == (1460 * double):
        	lookX = lookX - camX
        	lookY = lookY - camY
        	lookZ = lookZ - camZ
        	maxLook = max(lookX, lookY, lookZ)
        	lookX = lookX / maxLook
        	lookY = lookY / maxLook
        	lookZ = lookZ / maxLook
        	lookX = camX + lookX
        	lookY = camY + lookY
        	lookZ = camZ + lookZ
        	lookZ = lookZ - (0.01 * half)
        elif i < (1575 * double):
        	lookZ = lookZ + (0.01 * half)
        	lookX = lookX - (0.01 * half)
        elif i < (1645 * double):
        	camX = camX - (0.00224 * half)
        	camZ = camZ + (0.024507972 * half)
        	lookX = lookX - (0.00224 * half)
        	lookZ = lookZ + (0.024507972 * half)
        elif i < (1685 * double):
        	camX = camX - (0.00224 * half)
        	camZ = camZ + (0.024507972 * half)
        	camY = camY - (0.01 * half)
        	lookX = lookX + (0.02 * half)
        elif i < (1705 * double):
        	camX = camX + (0.0154368 * half)
        	camZ = camZ + (0.010538428 * half)
        	camY = camY + (0.005348998 * half)
        	lookX = lookX + (0.0154368 * half)
        	lookZ = lookZ + (0.010538428 * half)
        	lookY = lookY + (0.005348998 * half)
        elif i < (1712 * double):
        	lookZ = lookZ - (0.010538428 * half)
        	camZ = camZ - (0.010538428 * half)
        elif i < (1800 * double):
        	camX = camX + (0.011028588 * half)
        	camZ = camZ + (0.014992 * half)
        	camY = camY + (0.011028588 * half)
        	lookX = lookX + (0.011028588 * half)
        	lookZ = lookZ + (0.014992 * half)
        	lookY = lookY + (0.011028588 * half)
        elif i < (1820 * double):
            camX = camX + ((0.011028588 * 0.5) * half)
            camZ = camZ + ((0.014992 * 0.5) * half)
            camY = camY + ((0.011028588 * 0.5) * half)
            lookX = lookX + ((0.1 * 0.5) * half)
            lookY = lookY + ((0.011028588 * 0.5) * half)
        elif i < (1850 * double):
            camX = camX + ((0.011028588 * 0.5) * half)
            camZ = camZ - ((0.014992 * 0.5) * half)
            lookX = lookX + ((0.01 * 0.5) * half)
            lookZ = lookZ - ((0.014992 * 0.5) * half)
            lookY = lookY + ((0.011028588 * 0.5) * half)
        elif i < (2000 * double):
            camX = camX + ((0.011028588 * 0.25) * half)
            camZ = camZ - ((0.014992 * 0.25) * half)
            lookX = lookX + ((0.01 * 0.25) * half)
            lookZ = lookZ + ((0.014992 * 0.25) * half)
        elif i < (2050 * double):
            lookX = lookX + (0.01 * half)
            lookZ = lookZ + (0.014992 * half)
        elif i < (2350 * double):
            lookX = lookX + (0.02 * half)
            lookZ = lookZ - (0.02 * half)
        elif i < (2380 * double):
            lookX = lookX + (0.035 * half)
            lookZ = lookZ - (0.035 * half)
        elif i < (2440 * double):
            camX = camX + ((0.06113542166667 * 0.1) * half)
            camY = camY + ((0.00304442612473 * 0.1) * half)
            camZ = camZ + ((-0.02967914357087 * 0.1) * half)
            lookX = lookX + ((0.09668834496 * 0.1) * half)
            lookY = lookY + ((0.03660440194767 * 0.1) * half)
            lookZ = lookZ + ((0.0022329410744 * 0.1) * half)
        elif i < (2460 * double):
            camX = camX + ((0.06113542166667 * 0.1) * half)
            camY = camY + ((0.00304442612473 * 0.1) * half)
            camZ = camZ + ((-0.02967914357087 * 0.1) * half)
            lookX = lookX - ((0.09668834496) * half)
        elif i < (2480 * double):
            camX = camX + ((0.06113542166667 * 0.1) * half)
            camY = camY + ((0.00304442612473 * 0.1) * half)
            camZ = camZ + ((-0.02967914357087 * 0.1) * half)
            lookX = lookX - ((0.3) * half)
        elif i < (2520 * double):
            camX = camX + ((0.00172841732346 * 0.25) * half)
            camY = camY + ((0.00122351283196 * 0.25) * half)
            camZ = camZ + ((-0.00892266722326 * 0.25) * half)
            lookX = lookX + ((0.01362922982912 * 0.25) * half)
            lookY = lookY + ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2545 * double): # Going under chunk
            camX = camX + ((0.00172841732346 * 0.25) * half)
            camY = camY - ((0.00122351283196 * 0.25) * half)
            camZ = camZ + ((-0.00892266722326 * 0.25) * half)
            lookX = lookX + ((0.01362922982912 * 0.25) * half)
            lookY = lookY + ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2560 * double): # Coming back up from under the chunk
            camX = camX + ((0.00772841732346 * 0.25) * half)
            camY = camY + ((0.00122351283196 * 0.25) * half)
            camZ = camZ - ((0.00892266722326 * 0.25) * half)
            lookX = lookX - ((0.03362922982912 * 0.25) * half)
            lookY = lookY + ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2600 * double): # Rotating to view cube
            camX = camX + ((0.00772841732346 * 0.25) * half)
            camY = camY + ((0.00122351283196 * 0.25) * half)
            camZ = camZ - ((0.00892266722326 * 0.25) * half)
            lookX = lookX - ((0.08362922982912 * 0.25) * half)
            lookY = lookY + ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2630 * double): # Rotating more sharply (and going farther away)
            camX = camX + ((0.01272841732346 * 0.25) * half)
            camY = camY + ((0.00122351283196 * 0.25) * half)
            camZ = camZ - ((0.0192266722326 * 0.25) * half)
            lookX = lookX - ((0.12362922982912 * 0.25) * half)
            lookY = lookY - ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2650 * double): # Rotating more sharply (and going farther away)
            camX = camX + ((0.03272841732346 * 0.25) * half)
            camY = camY + ((0.00122351283196 * 0.25) * half)
            camZ = camZ - ((0.0192266722326 * 0.25) * half)
            lookX = lookX - ((0.12362922982912 * 0.25) * half)
            lookY = lookY - ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2700 * double): # Rotating more sharply (and going farther away)
            camX = camX + ((0.03272841732346 * 0.25) * half)
            #camY = camY + ((0.00122351283196 * 0.25) * half)
            #camZ = camZ - ((0.0192266722326 * 0.25) * half)
            lookX = lookX - ((0.12362922982912 * 0.25) * half)
            lookY = lookY - ((0.01142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2800 * double): # going farther away
            camX = camX + ((0.09272841732346 * 0.25) * half)
            lookX = lookX - ((0.12362922982912 * 0.25) * half)
            lookY = lookY - ((0.03142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2840 * double): # going farther away
            camX = camX + ((0.11272841732346 * 0.25) * half)
            lookX = lookX - ((0.02362922982912 * 0.25) * half)
            lookY = lookY - ((0.06542057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2860 * double): # going farther away
            camX = camX + ((0.11272841732346 * 0.25) * half)
            #lookX = lookX - ((0.02362922982912 * 0.25) * half)
            lookY = lookY - ((0.06542057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2900 * double): # going farther away
            camX = camX + ((0.11272841732346 * 0.25) * half)
            lookY = lookY - ((0.1142057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (2960 * double):
            camX = camX + ((0.11272841732346 * 0.25) * half)
            lookY = lookY - ((0.1942057340768 * 0.25) * half)
            lookZ = lookZ + ((0.0006927048846 * 0.25) * half)
        elif i < (3100 * double):
            camX = camX - ((0.02723653718023) * half)
            camY = camY - ((0.01037901589512) * half)
            camZ = camZ - ((0.00774632704047) * half)
            lookX = lookX - ((0.00008813160123) * half)
            lookY = lookY - ((0.0001091534347) * half)
            lookZ = lookZ + ((0.00085895405691) * half)
        elif i < (3250 * double):
            camX = camX - ((0.02723653718023 * 0.7) * half)
            camY = camY - ((0.01037901589512 * 0.7) * half)
            camZ = camZ - ((0.00774632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3300 * double):
            camX = camX - ((0.02723653718023 * 0.7) * half)
            camY = camY - ((0.01237901589512 * 0.7) * half)
            camZ = camZ + ((0.0124632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3330 * double):
            camX = camX - ((0.008723653718023 * 0.7) * half)
            camY = camY - ((0.01237901589512 * 0.7) * half)
            camZ = camZ - ((0.0124632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3340 * double):
            camX = camX - ((0.005723653718023 * 0.7) * half)
            camY = camY - ((0.02237901589512 * 0.7) * half)
            camZ = camZ + ((0.0124632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3350 * double):
            camX = camX - ((0.0105723653718023 * 0.7) * half)
            #camY = camY - ((0.02237901589512 * 0.7) * half)
            #camZ = camZ + ((0.0124632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3360 * double):
            camX = camX - ((0.0105723653718023 * 0.7) * half)
            camY = camY - ((0.02237901589512 * 0.7) * half)
            camZ = camZ + ((0.0024632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3370 * double):
            camX = camX - ((0.0085723653718023 * 0.7) * half)
            camY = camY - ((0.002237901589512 * 0.7) * half)
            camZ = camZ + ((0.014632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3380 * double):
            camX = camX - ((0.0087723653718023 * 0.7) * half)
            camY = camY - ((0.002237901589512 * 0.7) * half)
            camZ = camZ + ((0.0104632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3390 * double):
            camX = camX - ((0.0087723653718023 * 0.7) * half)
            camY = camY - ((0.003237901589512 * 0.7) * half)
            #camZ = camZ + ((0.0104632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3400 * double):
            camX = camX - ((0.0087723653718023 * 0.7) * half)
            camY = camY - ((0.005237901589512 * 0.7) * half)
            camZ = camZ + ((0.00504632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.7) * half)
        elif i < (3420 * double):
            camX = camX - ((0.0087723653718023 * 0.7) * half)
            camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ + ((0.00504632704047 * 0.7) * half)
            lookX = lookX - ((0.00008813160123 * 0.7) * half)
            lookY = lookY - ((0.0001091534347 * 0.7) * half)
            lookZ = lookZ - ((0.00085895405691 * 0.7) * half)
        elif i < (3440 * double):
            camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX - ((0.00008813160123 * 0.3) * half)
            lookY = lookY + ((0.0001091534347 * 0.3) * half)
            lookZ = lookZ + ((0.00085895405691 * 0.3) * half)
        elif i < (3460 * double):
            #camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX - ((0.08813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.085895405691) * half)
        elif i < (3480 * double):
            #camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX - ((0.10813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.1085895405691) * half)
        elif i < (3490 * double):
            #camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX - ((0.20813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.2085895405691) * half)
        elif i < (3500 * double):
            #camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX - ((0.60813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.6085895405691) * half)
        elif i < (3510 * double):
            #camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX - ((0.99813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.9985895405691) * half)
        elif i < (3520 * double):
            #camX = camX - ((0.011723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX + ((0.99813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.9985895405691) * half)
        elif i < (3530 * double):
            camX = camX - ((0.0031723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX + ((0.49813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ - ((0.4985895405691) * half)
        elif i < (3560 * double):
            #camX = camX - ((0.0031723653718023 * 0.3) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            lookX = lookX + ((1.49813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            lookZ = lookZ + ((1.4985895405691) * half)
        elif i < (3610 * double):
            camX = camX + ((0.0031723653718023 * 0.4) * half)
            #camY = camY - ((0.005237901589512 * 0.7) * half)
            #camZ = camZ - ((0.00504632704047 * 0.3) * half)
            #lookX = lookX + ((1.49813160123) * half)
            #lookY = lookY + ((0.01091534347) * half)
            #lookZ = lookZ + ((1.4985895405691) * half)


        # x = -14.80846970445 / 500 = -0.01480846970445
        # y = -1.5152030034523 / 500 = -0.00151520300345
        # z = -36.6674690782 / 500 = -0.0366674690782

        # lookX = -0.0440658006145 / 500 = -0.00008813160123
        # lookY = -0.0545767173497 / 500 = -0.0001091534347
        # lookZ = 0.429477028453 / 500 =  0.00085895405691

        n = str(i)
        if i <= 9:
            filenameDAT = 'params' + n.rjust(5-len(n),'0') + '.dat'
            filenameBMP = 'f' + n.rjust(5-len(n),'0') + '.bmp'
        elif i <= 99:
            filenameDAT = 'params' + n.rjust(6-len(n),'0') + '.dat'
            filenameBMP = 'f' + n.rjust(6-len(n),'0') + '.bmp'
        else:
            filenameDAT = 'params' + n.rjust(7-len(n),'0') + '.dat'
            filenameBMP = 'f' + n.rjust(7-len(n),'0') + '.bmp'
        file = open(filenameDAT, 'w+')
        fileStuff = '# CAMERA \n# location  camX,camY,camZ  \n'
        fileStuff = fileStuff + str(camX) + ' ' + str(camY) + ' ' + str(camZ) + '\n'
        fileStuff = fileStuff + '# look_at (target)  x y z \n'
        fileStuff = fileStuff + str(lookX) + ' ' + str(lookY) + ' ' + str(lookZ) + '\n' + \
        '# up vector camX,camY,camZ;  (0, 1, 0) \n' + \
        str(upX) + ' ' + str(upY) + ' ' + str(upZ) + ' \n' + \
        '# field of view     (1) \n' + \
        '1.1  \n' + \
        '# IMAGE \n' + \
        '# width height \n' + \
        '3840 2160 \n' + \
        '# detail level, the smaller the more detailed (-3) \n' + \
        '-3.5 \n' + \
        '# MANDELBOX \n' + \
        '# scale, rMin, rFixed  (2 0.5 1) \n' + \
        '2.0 0.5 1 \n' + \
        '# max number of iterations, escape time \n' + \
        '18 100 \n' + \
        '# COLORING \n' + \
        '# type 0 or 1 \n' + \
        '0 \n' + \
        '# brightness \n' + \
        '1.2 \n' + \
        '# super sampling anti aliasing 0 = off, 1 = on \n' + \
        '0 \n' + \
        '# IMAGE FILE NAME \n' + filenameBMP

        # 3840 2160
        # 640 480
        
        file.write(fileStuff)
        file.close()
main()
