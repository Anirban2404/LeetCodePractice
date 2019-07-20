#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:32:26 2019

@author: anirban-mac
"""
"""
443. String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the 
original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length 
of the array.

 
Follow up:
Could you solve it using only O(1) extra space?
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: 
    ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: 
    ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" 
is replaced by "b12".
Notice each digit has it's own entry in the array.
"""


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
#        count = 1
#        res = []
#        if len(chars) == 0:
#            return ''
#        
#        for i in range(1,len(chars)):
#            if chars[i] == chars[i-1]:
#                count += 1
#            else:
#                res.append(chars[i-1])
#                res.append(str(count))
#                count = 1
#                
#        res.append(chars[i])
#        res.append(str(count))
#        return (res)

        anchor = 0
        mod = 0
        length = len(chars)
        for i in range(length):
            if i + 1 == length or chars[i + 1] != chars[i]:
                chars[mod] = chars[anchor]
                mod += 1
                if i > anchor:
                    for count in str(i - anchor + 1):
                        chars[mod] = count
                        mod += 1
                anchor = i + 1
        print(chars)
        return mod
#        
chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","d"]
print(Solution().compress(chars))