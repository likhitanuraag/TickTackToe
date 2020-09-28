# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:52:40 2020

@author: Likhit
"""
import numpy as np
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
                        else:
                            print("Position of the value is occupied, please enter right value")
                    i += 1
                    
            print(t)