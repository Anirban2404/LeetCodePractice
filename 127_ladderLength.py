#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:10:39 2019

@author: anirban-mac
"""

"""
127. Word Ladder
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that beginWord is not 
a transformed word.
Note:

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" 
-> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible 
transformation.
"""
from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
            
        length = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(length):
                all_combo_dict[word[:i] + "_" + word[i+1:]].append(word)
        print(all_combo_dict)
            
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        print(visited)
        while queue:
            curr, level = queue.popleft()
            print("-#->", curr)
            for i in range(length):
                intermediate_word = curr[:i] + "_" + curr[i+1:]
                print("-#->",intermediate_word)
                for word in all_combo_dict[intermediate_word]:
                    print("-->", word, "-->", all_combo_dict[intermediate_word])
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                    print(visited)
                all_combo_dict[intermediate_word] = []
        return 0
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))