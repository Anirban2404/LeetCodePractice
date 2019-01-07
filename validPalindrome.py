#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:18:36 2019

@author: anirban-mac
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:07:02 2019

@author: anirban-mac
"""
"""
Given a string, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverseString = []
        s = re.compile('[^a-zA-Z0-9]').sub('', s).lower()
        print(s)
        origString = list(s)
        for i in range(len(origString)-1,-1,-1):
           reverseString.append(origString[i]) 
        
        reverseString = ''.join(reverseString)
        print(reverseString)
        if reverseString == s:
            return True
        else:
            return False
        
    def isPalindrome2(self, s):
        
        s = re.compile('[^a-zA-Z0-9]').sub('', s).lower()
        left = 0
        right = len(s)-1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            else: 
                left +=1
                right -= 1
            
        return True

s = "race a car"
print(Solution().isPalindrome(s))
print(Solution().isPalindrome2(s))