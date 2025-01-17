# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:52:40 2020

@author: Likhit
"""
import numpy as np
import sys

def similarList(list):
    return all(x == list[0] for x in list)

def goalCheck(arr, player):
    for l in range(n):
        kk = []
        if (t[l] == player).all() and ("*" not in kk):
            #Horizontal check
            return True
        for m in range(n):
            kk.append(arr[m, l])
        if (similarList(kk) == True) and ("*" not in kk):
            #vertical check
            return True
        else:
            continue
    dd1 = []
    dd2 = []
    for d in range(n):
        dd1.append(arr[n-(d+1), d])
        dd2.append(arr[d, d])
    if (similarList(dd1) == True) or (similarList(dd2) == True):
        if ("*" not in dd1) or ("*" not in dd2):
            #Diagonal check
            return True
        else:
            pass

def Winner(player):
    BoolWin = True
    print(t)
    print(f"the winner is {player}")
    if input("If you want to play the game again, press enter. If not, type exit to exit: ") == "":
        sys.exit()
    while (BoolWin):
        BoolWin = True

def Inserter(player):
    global Bool 
    try:
        pos_val = int(input(f"Enter position for player {player}: "))
    except ValueError:
        print("please enter a valid number")    
    i = 1
    for j in range(n):
        for k in range(n):
            if (i == pos_val):
                if (t[j, k] == "*"):
                    t[j, k] = player
                    Bool = False
                    if (goalCheck(t, player)):
                        Winner(player)
                else:
                    print("Position of the value is occupied, please enter right value")
            i += 1                   
    print(t)


n = int(input("enter the dim: "))
t = np.full((n,n), "*")
print(t)
#r = range(0, n*n)
for game_loop in range(n*n):
    Bool = True
    while (Bool):
        if ((game_loop+1) % 2) != 0:  
            Inserter("X")  
        else:    
            Inserter("O")

if input("If you want to play the game again, press enter. If not, type exit to exit: ") == "":
    sys.exit()