# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

nemo = ["hulo","nemo"]
#for i in range(100000):
#    nemo.append("demo")
    
def findnemo(arr):
    start = time.time()
    nemo = arr
    for i in nemo:
        if (i=="nemo"):
            print("Found Nemo:)")
        else:
            print(":(")
    end = time.time()
    print ("time_taken in seconds: ", end - start)

findnemo(nemo)