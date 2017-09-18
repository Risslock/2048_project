# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:09:41 2017

@author: Juan E
"""

#from random import randint
from BaseAI_3 import BaseAI
import time
import math

timeLimit = 0.1
safety = 0.01
#nodes=0


class PlayerAI(BaseAI):
#    def getMove(self,grid):
#        moves=grid.getAvailableMoves()
#        return moves[randint(0,len(moves)-1)] if moves else None

    def __inti__(self):
        self.startTime = 0
        self.over = False
        
    def smoothness(self,grid):
        smooth = 0
        SM = 0
#        print(grid.map)
        for x in range(3):
            for y in range(3):
                    value_1 = grid.getCellValue((x,y))
                    value_2 = grid.getCellValue((x,y+1))
                    SM = abs(value_1-value_2)
            smooth -= SM
        for y in range(3):
            for x in range(3):
                    value_1 = grid.getCellValue((x,y))
                    value_2 = grid.getCellValue((x+1,y))
                    SM = abs(value_1-value_2)
            smooth -= SM
        return smooth
    
    def monotonicity(self,grid):
        #Try to get the max value on the upper left corner
#        Weigth_mat=[[65535,32768,16384,8192],[512,1024,2048,4096],[256,128,64,32],[2,4,8,16]]
#        r=0.5
#        mat=[[1,2,3,4],[8,7,6,5],[9,10,11,12],[16,15,14,13]]
#        mat2=[[1,8,9,16],[2,7,10,15],[3,6,11,14],[4,5,12,13]]


        Weigth_mat=[[65535,16348,4096,512],[16348,4096,512,128],[4096,1024,128,32],[512,128,16,4]]
        mono_sum = 1
#        mono_sum2 = 1
        for x in range(3):
            for y in range(3):
                mono_sum += grid.getCellValue((x,y))*Weigth_mat[x][y]
#                mono_sum += grid.getCellValue((x,y))*pow(r,mat[x][y])
#                mono_sum2 += grid.getCellValue((x,y))*pow(r,mat2[x][y])
                

#        if mono_sum<mono_sum2:
#            mono_sum= mono_sum2
#        print("mono_sum",mono_sum)
        return math.log(mono_sum)
#        return mono_sum
    
#    def monotonicity2(self,grid):
#        ratio=0.5
        
                
         
    def Eval(self,grid):
#        smoothWeight = 0.0002
#        emptyWeight = 0.02
        maxWeight = 0.51
        monoWeight = 1
#        emptyCells=len(grid.getAvailableCells())
#        smoothness=self.smoothness(grid)
        monotonicity = self.monotonicity(grid)
#        utility = grid.getMaxTile()*maxWeight+math.log(emptyCells+0.01)*emptyWeight+smoothness*smoothWeight+monotonicity*monoWeight
#        utility = smoothness*smoothWeight+monotonicity*monoWeight
#        if emptyCells <= 3:
#            utility = monotonicity*monoWeight+grid.getMaxTile()*maxWeight+math.log(emptyCells+1)*emptyWeight
#        else:
        utility = monotonicity*monoWeight+grid.getMaxTile()*maxWeight
                                                             
#        print("smoothness",smoothness)
#        print("monotonicity",monotonicity)
#        print("Max tile",grid.getMaxTile())
#        print("Empy Cells",emptyCells)
#        print("Utility",utility)
        return utility
    
    def getMove(self,grid):
        global nodes
        maxDepth=1
        time_off=0
        self.startTime = time.clock()        
        while time.clock()-self.startTime<timeLimit-safety:
            alpha = -100000
            beta = 100000
            maxDepth+=1
#            nodes=0
            (child,utility)=self.Maximize(grid,maxDepth,alpha,beta,time_off)
            if child == None:
                break
            else:
                bestMove=child
                bestUtility=utility
            
#        print("max depth ",maxDepth)
#        print("Best Utility", bestUtility)
#            print("getmove",time.clock()-self.prevTime)
#            print("nodes visited",nodes)
#        print (time.clock())
        return bestMove
    
    def Maximize(self,grid,depth,alpha, beta,time_off):
#        global nodes
        global timeLimit
        global safety
#        if depth==0:
#            return (None,self.Eval(grid))

        if time.clock()-self.startTime>=timeLimit-safety:
            time_off=1
            return (None,self.Eval(grid))        
        if depth==0:
            return (None,self.Eval(grid))

        (maxChild,maxUtility)=(None,-10000)
        
        for direction in grid.getAvailableMoves():
            newGrid=grid.clone()
            newGrid.move(direction)
            if time_off==1:
                return (maxChild,maxUtility)

            (_,utility)=self.Minimize(newGrid,depth-1,alpha,beta,time_off)
#            if time.clock()-self.prevTime>=timeLimit-safety:
#                return (maxChild,maxUtility)

            if utility>maxUtility:
                (maxChild,maxUtility)=(direction,utility)
#                nodes += 1
            if maxUtility>= beta:
#                nodes += 1
                break
            if maxUtility>alpha:
                alpha=maxUtility

        return (maxChild,maxUtility)
    
    def Minimize(self,grid,depth, alpha, beta,time_off):
#        global nodes
        global timeLimit
        global safety
#        if depth==0:
#            return (None,self.Eval(grid))

        if time.clock()-self.startTime>=timeLimit-safety:
            time_off=1
            return (None,self.Eval(grid))       
        if depth==0:
            return (None,self.Eval(grid))

        
        (minChild,minUtility)=(None,10000)
        
        scores = {2:[]}
        for value in scores: 
            if time_off==1:
                return (minChild,minUtility)
            for cells in grid.getAvailableCells():
                if time_off==1:
                    return (minChild,minUtility)
                newGrid=grid.clone()
                newGrid.insertTile(cells,value)

            
                (_,utility)=self.Maximize(newGrid,depth-1,alpha,beta,time_off)
#                if time.clock()-self.prevTime>=timeLimit-safety:
#                    return (minChild,minUtility)
                if utility<minUtility:
                    (minChild,minUtility)=(cells,utility)
#                    nodes += 1                    
                if minUtility<= alpha:
#                    nodes += 1
                    break
                if minUtility<beta:
                    beta=minUtility


        return (minChild,minUtility)        
        
            
        
