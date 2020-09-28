# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:52:40 2020

@author: Likhit
"""
import numpy as np
n = int(input("enter the dim: "))
t = np.full((n,n), "*")
print(t)
pos_val = int(input("value of the position: "))

i = 1
for j in range(n):
    for k in range(n):
        #print(j, k, i)
        if i == pos_val:
            t[j, k] = "X"
        i += 1
        
print(t)