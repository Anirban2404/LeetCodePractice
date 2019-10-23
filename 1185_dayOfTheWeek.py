#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:47:49 2019

@author: anirban-mac
"""

"""
1185. Day of the Week
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year 
respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", 
"Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
"""

from datetime import date
class Solution:
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        ans = date(year, month, day)
        print (ans.strftime("%A"))
        days = { 
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"
               }
        
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#        if day > daysInMonth[month - 1]:
#            return False
#        
        count = 0
        for yr in range(1,year):
            if self.check_leapyear(yr):
                count +=1
        print(count)
        
        tot_days = 365 * (year - 1) + count
        
        if month > 2:
            if self.check_leapyear(year):
                tot_days += 1
               
        if month > 1:   
            print(daysInMonth[:month - 1])
            tot_days += sum(daysInMonth[:month - 1])
        
        tot_days += day - 1
        rem = tot_days % 7
        
        return (days[rem])
        #print(tot_days)
        
    def check_leapyear(self, year):
        if year % 400 == 0 or ( year % 4 == 0  and year %100 != 0):
            return True
        return False
            
    
day = 29
month = 2
year = 2016

print(Solution().dayOfTheWeek(day, month, year))