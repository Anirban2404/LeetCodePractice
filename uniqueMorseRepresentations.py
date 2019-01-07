#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:05:50 2019

@author: anirban-mac
"""
"""
International Morse Code defines a standard encoding where each letter is 
mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" 
maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet 
is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
"--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--",
"--.."]
Now, given a list of words, each word can be written as a concatenation of the 
Morse code of each letter. For example, "cba" can be written as "-.-..--...", 
(which is the concatenation "-.-." + "-..." + ".-"). We'll call such a 
concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        
        morseCodesChar = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                          ".---","-.-",".-..","--","-.","---",".--.","--.-",
                          ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        morseSet = set()
        
        for word in words:
            wordlist = list(word)
            morsestr = ""
            for ch in wordlist:
                morsestr = morsestr + (morseCodesChar[ord(ch)-(ord('a'))])
            #print(morsestr)
            morseSet.add(morsestr)
        return(len(morseSet))
        
words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))