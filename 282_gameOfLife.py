#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:18:48 2019

@author: anirban-mac
"""

"""
289. Game of Life
According to the Wikipedia's article: "The Game of Life, also known simply as 
Life, is a cellular automaton devised by the British mathematician John Horton 
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or 
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, 
diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by 
reproduction.
Write a function to compute the next state (after one update) of the board given 
its current state. The next state is created by applying the above rules 
simultaneously to every cell in the current state, where births and deaths occur 
simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the 
same time: You cannot update some cells first and then use their updated values 
to update other cells.
In this question, we represent the board using a 2D array. In principle, the 
board is infinite, which would cause problems when the active area encroaches 
the border of the array. How would you address these problems?
"""
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        nrows = len(board)
        ncols = len(board[0])

        tempboard = [[i for i in row] for row in board]
        for row in range(nrows):
            #print(tempboard[row])
            for col in range(ncols):
                count = 0
                for _dir in directions:
                    x = row + _dir[0]
                    y = col + _dir[1]
                    if x < 0 or y < 0 or x >= nrows or y >= ncols:
                        continue
                    if tempboard[x][y] == 1:
                        count += 1
                #print("COUNT:", count)
                """
                1. Any live cell with fewer than two live neighbors dies, 
                as if caused by under-population.
                """
                if count < 2:
                    if tempboard[row][col] == 1:
                        board[row][col] = 0
                """
                2. Any live cell with two or three live neighbors lives on to 
                the next generation.
                """
                if 2 >= count >= 3:
                    if tempboard[row][col] == 1:
                        board[row][col] = 1
                """
                3. Any live cell with more than three live neighbors dies, as 
                if by over-population.
                """
                if count > 3:
                    if tempboard[row][col] == 1:
                        board[row][col] = 0
                """
                4. Any dead cell with exactly three live neighbors becomes a 
                live cell, as if by reproduction.
                """
                if count == 3:
                    if tempboard[row][col] == 0:
                        board[row][col] = 1
                
        return (board)


    

        
        
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(Solution().gameOfLife(board))