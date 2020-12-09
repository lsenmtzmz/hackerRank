#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:55:31 2020

@author: enrique
"""

### Problema Solving (Intermediate)
## Solución del ejercicio para certificación - Betwise And

import itertools
import math

def countPairs(arr):
    # Write your code here
    comb = itertools.combinations(arr, 2) 
    counter = 0
    for n,k in comb:
        if (n & k) != 0 and math.log((n & k), 2).is_integer():
                print(n,k)
                counter += 1

    return(counter)

arr1 = [10,7,2,8,3]
arr2 = [1,2,1,3]

countPairs(arr2)
