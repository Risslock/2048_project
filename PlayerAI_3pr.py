# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:09:41 2017

@author: Juan E
"""

from random import randint
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
#    def getMove(self,grid):
#        moves=grid.getAvailableMoves()
#        return moves[randint(0,len(moves)-1)] if moves else None
    
    def getMove(self,grid):
        alpha= -10000
        beta= 10000
        (child,_)=self.Maximize(grid,alpha,beta)
        return child
    
    def Maximize(self,grid,alpha, beta):
        
        
#        if Terminal_test(grid):
#            return (None,Eval(grid))
        (maxChild,maxUtility)=(None,-10000)
        
        for direction in grid.getAvailableMoves():
            newGrid=grid.clone()
            
            (_,utility)=self.Minimize(newGrid.move(direction),alpha,beta)
            if utility>maxUtility:
                (maxChild,maxUtility)=(direction,utility)
            if maxUtility>= beta:
                break
            if maxUtility>alpha:
                alpha=maxUtility
        return (maxChild,maxUtility)
    
    def Minimize(self,grid,alpha,beta):
#        if Terminal_test(grid):
#            return (None,Eval(grid))
        
        (minChild,minUtility)=(None,10000)
        
        
        
        for cells in grid.getAvailableCells():
            newGrid=grid.clone()
            newGrid.insertTile()

            
            (_,utility)=self.Maximize(newGrid.move(direction),alpha,beta)
            if utility>minUtility:
                (minChild,minUtility)=(direction,utility)
            if minUtility<= alpha:
                break
            if minUtility<beta:
                beta=minUtility
        return (minChild,minUtility)        
        
            
        
