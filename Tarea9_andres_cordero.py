# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:21:05 2022

@author: adsc9
"""


print("------#Ejercicio 2.6------")

def Luhn(para):
    nd = len(para)
    s = 0
    se = False
    for i in range(nd - 1, -1, -1):
        d = ord(para[i]) - ord('0')
        if (se == True):
            d = d * 2
        s += d // 10
        s += d % 10
        se = not se
    if (s % 10 == 0):
        return True
    else:
        return False
    

  




