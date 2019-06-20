#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:46:52 2019

@author: anirban-mac
"""

"""
126. Word Ladder II
Given two words (beginWord and endWord), and a dictionary's word list, find all 
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a 
transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible 
transformation.
"""
from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []
            
        length = len(beginWord)
        lookupDict = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                lookupDict[word[:i] + '_' + word[(i+1):]].append(word)
    
        minDists = {word: len(wordList) for word in wordList}
        print(minDists)
        minDists[beginWord] = 1
        
        q = deque([(beginWord, 1, [beginWord])]) # node, path length, path: List[node]
        paths = []
        minDesDist = len(wordList)
        
        while q:
            curr_word, dist, path = q.popleft()
            for i in range(length):
                for word in lookupDict[curr_word[:i] + '_' + curr_word[(i+1):]]:
                    if word != curr_word and dist + 1 <= minDists[word]:
                        if word != endWord:
                            minDists[word] = dist + 1
                            q.append([word, dist + 1, path + [word]])
                            print(minDists)
                        else:
                            if dist + 1 <= minDesDist:
                                paths.append(path + [word])
                                minDesDist = dist + 1
                            
        return paths
                       

    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot", "dog","lot","log","cog"]
print(Solution().findLadders(beginWord, endWord, wordList))