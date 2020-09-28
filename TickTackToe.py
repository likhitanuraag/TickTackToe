# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:52:40 2020

@author: Likhit
"""
import numpy as np

def similarList(list):
    return all(x == list[0] for x in list)

def goalCheck(arr, player):
    for l in range(n):
        kk = []
        if (t[l] == player).all() and ("*" not in kk):
            #Horizontal check
            print("hori")
            return True
        for m in range(n):
            kk.append(arr[m, l])
        if (similarList(kk) == True) and ("*" not in kk):
            #vertical check
            print("verti")
            return True
        else:
            continue
    dd1 = []
    dd2 = []
    for d in range(n):
        dd1.append(arr[n-(d+1), d])
        dd2.append(arr[d, d])
        print(dd2)
    if (similarList(dd1) == True) or (similarList(dd2) == True):
        if ("*" not in dd1) or ("*" not in dd2):
            #Diagonal check
            print("diag")
            return True
        else:
            pass

def Winner(player):
    BoolWin = True
    print(t)
    print(f"the winner is {player}")
    while (BoolWin):
        BoolWin = True



n = int(input("enter the dim: "))
t = np.full((n,n), "*")
print(t)
#r = range(0, n*n)
for game_loop in range(n*n):
    Bool = True
    while (Bool):
        if ((game_loop+1) % 2) != 0:  
            try:
                pos_val = int(input("Enter position for player X: "))
            except ValueError:
                print("please enter a valid number")    
            i = 1
            for j in range(n):
                for k in range(n):
                    #print(j, k, i)
                    if (i == pos_val):
                        if (t[j, k] == "*"):
                            t[j, k] = "X"
                            Bool = False
                            if (goalCheck(t, "X")):
                                Winner("X")
                        else:
                            print("Position of the value is occupied, please enter right value")
                    i += 1
                    
            print(t)  
        else:    
            try:
                pos_val = int(input("Enter position for player O: "))
            except ValueError:
                print("please enter a valid number")    
            i = 1
            for j in range(n):
                for k in range(n):
                    #print(j, k, i)
                    if (i == pos_val):
                        if (t[j, k] == "*"):
                            t[j, k] = "O"
                            Bool = False
                            if (goalCheck(t, "O")):
                                Winner("O")
                        else:
                            print("Position of the value is occupied, please enter right value")
                    i += 1
                    
            print(t)