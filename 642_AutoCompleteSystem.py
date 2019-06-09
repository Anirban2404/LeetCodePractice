#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:37:29 2019

@author: anirban-mac
"""
"""

642. Design Search Autocomplete System
Design a search autocomplete system for a search engine. Users may input a 
sentence (at least one word and end with a special character '#'). For each 
character they type except '#', you need to return the top 3 historical hot
 sentences that have prefix the same as the part of sentence already typed. 
 Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed 
the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is 
the hottest one). If several sentences have the same degree of hot, you need 
to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this 
case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. 
The input is historical data. Sentences is a string array consists of previously 
typed sentences. Times is the corresponding times a sentence has been typed. 
Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will 
provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. 
The character will only be lower-case letters ('a' to 'z'), blank space (' ') 
or a special character ('#'). Also, the previously typed sentence should be 
recorded in your system. The output will be the top 3 historical hot sentences 
that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], 
[5,3,2,2])
The system have already tracked down the following sentences and their 
corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

    Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love 
leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII 
code 114, "i love leetcode" should be in front of "ironman". Also we only need 
to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical 
sentence in system. And the following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only 
one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length 
of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even 
for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem,
 as static/class variables are persisted across multiple test cases. Please see 
 here for more details.
"""
import collections
import heapq
class Node:
    def __init__(self):
        self.next=collections.defaultdict(Node)
        self.wordDict=collections.defaultdict(int)

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root=Node()
        for i in range(len(sentences)):
            self.buildWord(sentences[i], times[i])
        self.searchRoot=self.root
        self.searchWord=''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        print("-->", c)
        if c=='#':
            self.buildWord(self.searchWord, 1)
            self.searchWord=''
            self.searchRoot=self.root
            return []
        self.searchWord+=c
        self.searchRoot=self.searchRoot.next[c]
        # O(nlogn) sorting one line:
        print ([i[0] for i in sorted(self.searchRoot.wordDict.items(), \
                key=lambda i: (-i[1], i[0]))[:3]])
        # or O(n) using heap:
        hp=[(-v, k) for k, v in self.searchRoot.wordDict.items()]
        heapq.heapify(hp)
        res=[]
        for _ in range(3):
            if hp:
                res.append(heapq.heappop(hp)[1])
        return res
    
    def buildWord(self, word, time):
        self.cur=self.root
        for c in word:
            self.cur=self.cur.next[c]
            self.cur.wordDict[word]+=time
        
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)