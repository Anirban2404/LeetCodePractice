#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:28:08 2019

@author: anirban-mac
"""

"""
79. Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where 
"adjacent" cells are those horizontally or vertically neighboring. The same 
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])

        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
                
            if i < 0 or i >= m or j < 0 or j >= n or word[0]!=board[i][j]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"
            res =  dfs(board, i+1, j, word[1:]) \
                or dfs(board, i-1, j, word[1:]) \
                or dfs(board, i, j+1, word[1:]) \
                or dfs(board, i, j-1, word[1:])
            board[i][j] = tmp
            return res
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
        
    
    
board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
        ]
word = "ABCES"
print(Solution().exist(board, word))