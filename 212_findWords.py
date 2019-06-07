#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:02:21 2019

@author: anirban-mac
"""

"""
Given a 2D board and a list of words from the dictionary, find all words in the 
board.

Each word must be constructed from letters of sequentially adjacent cell, where 
"adjacent" cells are those horizontally or vertically neighboring. The same 
letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        print(word)
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    
class Solution:
    directions = {(0,1),(1,0),(0,-1),(-1,0)}
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0:
            return 0
        m = len(board)
        n = len(board[0])
        res = []
        
        #Trie
        trie = Trie()
        node = trie.root
        for word in words:
            print(word)
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                print(board)
                self.dfs(board, node, m, n, i , j, "", res)
        return res
    
    def dfs(self, board, node, m, n, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
            print(res)
            
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        
        tmp = board[i][j]
        print(tmp)
        node = node.children.get(tmp)
       
        if not node:
            return
        
        board[i][j] = "#"
        
        for d in self.directions:
            x = i + d[0]
            y = j + d[1]
            print(x,y)
            #if 0<=x<m and 0<=y<n:
            self.dfs(board, node, m, n, x, y, path+tmp, res)
            print(res)
        board[i][j] = tmp
        
        
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
board = [["a"]]
words = ["a"]
print(Solution().findWords(board, words))