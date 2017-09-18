# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 10:33:43 2017

@author: Juan E
"""
import GameManager_3 as GM

for x in range(25):
    
    gameManager = GM.GameManager()
    playerAI  	= GM.PlayerAI()
    computerAI  = GM.ComputerAI()
    displayer 	= GM.Displayer()

    gameManager.setDisplayer(displayer)
    gameManager.setPlayerAI(playerAI)
    gameManager.setComputerAI(computerAI)

    gameManager.start()