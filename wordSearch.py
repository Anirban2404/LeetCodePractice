#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:05:00 2019

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

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

@author: anirban-mac
"""

class wordSearch:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for alph in word:
            for i,letter in enumerate(board):
                print(letter)
                if alph in letter:
                    print(alph, "-->", i, letter.index(alph))
                    board[i][letter.index(alph)] = "*"
                #break
            #break

        
board =[
        ['A','B','C','E'], 
        ['S','F','C','S'],
        ['A','D','E','E']
        ]

word = "SBCCED"
print(wordSearch().exist(board, word))