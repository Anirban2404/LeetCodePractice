#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:57:18 2019

@author: anirban-mac
"""

"""
794. Valid Tic-Tac-Toe State
A Tic-Tac-Toe board is given as a string array board. Return True if and only 
if it is possible to reach this board position during the course of a valid 
tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The 
" " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always 
places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, 
column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
"""

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        countX = 0
        countO = 0
        
        FIRST = 'X'
        SECOND = 'O'
        
#        sum(row.count(FIRST) for row in board)
        for i in range(len(board)):

            if FIRST in board[i]:
                for j in board[i]:
                    if j == FIRST:
                        countX += 1 
            if SECOND in board[i]:
                 for j in board[i]:
                    if j == SECOND:
                        countO += 1

        if countO not in {countX - 1, countX}: 
            #print("Clause1")
            return False
        
        if self.winCheck(board, FIRST) and countX-1 != countO: 
            #print("Clause2")
            return False
        
        if self.winCheck(board, SECOND) and countX != countO: 
            #print("Clause3")
            return False

        return True
        
        return True        
        
    def winCheck(self, board, player):
        for i in range(len(board)):
            if all(board[i][j] == player for j in range(len(board[0]))):
                return True
            
            if all(board[j][i] == player for j in range(len(board[0]))):
                return True

        return (player == board[1][1] == board[0][0] == board[2][2] or
                player == board[1][1] == board[0][2] == board[2][0])

board = ["XXX", "   ", " OO"]
#board = ["X  ","   ","   "]
print(Solution().validTicTacToe(board))