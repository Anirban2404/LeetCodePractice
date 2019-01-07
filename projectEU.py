#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:00:40 2018

@author: anirban-mac
"""

def prob1(numRange):
    sum = 0
    for i in range(numRange):
        if ((i%3 == 0) or (i%5==0)):
            sum +=i
    return(sum)

print("Prob1: ", prob1(1000))

def prob2(numRange):
    sumarr = []
    sum = 1 
    sumfibeven = 0
    sumarr.append(0)
    sumarr.append(sum)
    
    limit = 4000000
            
    for i in range(1, numRange+1):
        sum = sumarr[i] + sumarr[i-1]
        sumarr.append(sum)
        
        if (sum>=limit):
            break
        if (sum %2 == 0):
            sumfibeven = sumfibeven + sum
#    print (sum)    
    return(sumfibeven)

print("Prob2: ", prob2(1000000))

import math 

def prob3(num):
    primefactors = []
    while (num%2 == 0):
       num = num/2
       primefactors.append(2)
    
       
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while (num%i == 0):
            num = num/i
            primefactors.append(i)
    primefactors.append(int(num))
    return (primefactors)

print("Prob3: ", max(set(prob3(600851475143))))
   
def prob4():
    maxi = 0
    for i in range(999, 100, -1):
        for j in range(999, int(999/2), -1):
           #print(i,j) 
           number = i*j
           #print(number)
           ispalindrome = checkpalindrome(number)
           #print(ispalindrome)
           if (ispalindrome):
               if (maxi<number):
                   maxi = number
                 
    return (maxi)



def checkpalindrome(orignumber):
    number = orignumber
    palindrome = False
    reversednum = 0
    
    while (number!= 0):
        reversednum = 10 * reversednum + number%10
        number = int(number/10) 
#    print (reversednum)
    if (reversednum == orignumber):
        palindrome = True
    else:
        palindrome = False
    return palindrome

print("Prob4: ", prob4())

#def prob5(numRange):
#    num = 1
#    hit = True
#    while (hit):
#        for i in reversed(range(1,numRange+1)):
#            #print(i)
#            if (num%i == 0):
#                #print("Divisible: ", i,num)
#                if (i == numRange/2):
#                    hit = False
#                else:
#                    continue
#            else:
#                #print("Not Divisible: ", i,num)
#                num += 1
#                break
#                
#    return num
#
#print("Prob5: ", prob5(20))